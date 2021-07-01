import os
import time
import requests

import pandas as pd
from lxml.html import fromstring

from ..utils.logging import *

__BASEURL = 'https://www.coupang.com'


def get_library(path):
    """
    get_library: read library data
    """
    library_df = pd.read_excel(path)
    library_dict = dict()
    for column in library_df.columns:
        library_dict[column] = library_df[column].dropna().drop_duplicates().tolist()

    return library_dict


def get_url_information(urlcrawl_baseurl, URLCRAWL_URL_XPATH, URLCRAWL_PRODUCT_XPATH,
                        urlcrawl_review_num_xpath, keyword, library, HEADERS):
    """
    get_url_information: Crawling information using Xpath for each page
    """
    res = requests.get(urlcrawl_baseurl.format(keyword), headers=HEADERS)
    parser = fromstring(res.text)

    # Crawling url
    elements = parser.xpath(URLCRAWL_URL_XPATH)
    url_list = [__BASEURL + element.findall('a')[0].get('href') for element in elements[:10]]

    # Crawling product name
    products = parser.xpath(URLCRAWL_PRODUCT_XPATH)
    product_list = [product.text_content() for product in products[:10]]

    # Crawling review nums
    review_list = list()
    for element_num in range(1,len(product_list)+1):
        try:
            review_num =\
                parser.xpath(urlcrawl_review_num_xpath.format(element_num))[0].text_content()[1:-1]
        except:
            review_num = '0'

        review_list.append(review_num)

    tmp = pd.DataFrame({
        'url':url_list,
        'review_count':review_list, 
    })

    tmp['product_name'] = product_list
    tmp['keyword'] = keyword
    tmp['library'] = library
    tmp['id'] = tmp['url'].apply(lambda x: x.split('/')[5].split('?')[0])

    return tmp


def url_cralwer(library_dict, HEADERS, urlcrawl_baseurl, URLCRAWL_URL_XPATH, URLCRAWL_PRODUCT_XPATH,
                urlcrawl_review_num_xpath, urldata_log_path, urldata_save_path):

    """
    url_crawler: URL Crawling Process
    """

    # Define dataframe
    df_final = pd.DataFrame()

    for library in library_dict.keys():

        df = pd.DataFrame()
        time.sleep(5)

        for keyword in library_dict[library]:

            try:
                tmp = get_url_information(urlcrawl_baseurl, URLCRAWL_URL_XPATH, URLCRAWL_PRODUCT_XPATH, 
                                        urlcrawl_review_num_xpath, keyword, library, HEADERS)
                df = df.append(tmp, ignore_index=True)

            # make_log
            except Exception as error:
                error_logging(urldata_log_path, library, keyword, error, 'url')
                time.sleep(3)

        # save per library
        os.makedirs(urldata_save_path.format(library), exist_ok=True)
        df = df[df['review_count'] != '0'].drop_duplicates(subset=['id']).reset_index(drop=True)
        dstpath = f'{urldata_save_path.format(library)}/{library}(url).csv'
        df.to_csv(dstpath, index=False, encoding='utf-8')
        df_final = df_final.append(df, ignore_index=True)

    return df_final
