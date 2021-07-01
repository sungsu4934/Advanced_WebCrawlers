import os
import time
import subprocess

import pandas as pd
from selenium import webdriver

from ..utils.logging import *


def detail_crawler(df_url, CHROME_EXE_PATH, CHROMEDRIVER_PATH, SELENIUM_OPTION, 
                   MOVE_XPATH1, MOVE_XPATH2, MOVE_XPATH3, MOVE_XPATH4, MOVE_XPATH5, 
                   MOTION1_XPATH, MOTION2_XPATH, MOTION3_XPATH, 
                   ELEMENTS_XPATH, NAME_XPATH, PRODUCT_XPATH, DATE_XPATH, STAR_XPATH, 
                   HEADLINE_CLASS_NAME, CONTENT_CLASS_NAME,
                   page_move_xpath, detaildata_save_path, detaildata_log_path):  

    """
    detail_crawler: Crawling for detail informations. 
    You may access to url which you get from url_crawling
    """

    # Reset values
    t1 = time.time()
    result_final = pd.DataFrame()
    result = pd.DataFrame()

    for url_idx in range(df_url.shape[0]):
        # Access by chrome.exe
        subprocess.Popen(CHROME_EXE_PATH) 

        # Access to url
        driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=SELENIUM_OPTION)
        url = df_url.loc[url_idx, 'url']
        keyword = df_url.loc[url_idx, 'keyword']
        library = df_url.loc[url_idx, 'library']
        driver.get(url)
        time.sleep(2)

        # Move Scroll: <필수 표기정보>
        try:
            location = driver.find_element_by_xpath(MOVE_XPATH1)
            driver.execute_script(f"window.scrollTo(0, {location.location['y']})")

        except Exception as error:
            error_logging(detaildata_log_path, library, url_idx, error, 'detail')
            driver.close()
            time.sleep(3)
            continue

        time.sleep(2)

        # Click: <상품평>
        driver.find_element_by_xpath(MOVE_XPATH2).click()
        time.sleep(2)

        # Move Scroll: <별점보기 칸>
        location2 = driver.find_element_by_xpath(MOVE_XPATH3)
        driver.execute_script(f"window.scrollTo(0, {location2.location['y']-300})")
        time.sleep(1)

        # Click: <별점보기>
        try:
            driver.find_element_by_xpath(MOVE_XPATH4).click()
            time.sleep(2)

        except:
            error_logging(detaildata_log_path, library, url_idx, error, 'detail')
            driver.close()
            continue

        # Click Each Motion (Score 1~3)
        motion1 = driver.find_element_by_xpath(MOTION1_XPATH)
        motion2 = driver.find_element_by_xpath(MOTION2_XPATH)
        motion3 = driver.find_element_by_xpath(MOTION3_XPATH)
        motions = [motion1, motion2, motion3]

        for motion in motions:

            # Reset Page
            page_value = 3

            # Click Motion
            motion.click()
            time.sleep(2)

            while True:
                try:
                    # Crawling
                    elements = driver.find_elements_by_xpath(ELEMENTS_XPATH)

                    for element in elements:
                        name = element.find_elements_by_xpath(NAME_XPATH)[0].text # writer
                        product = element.find_elements_by_xpath(PRODUCT_XPATH)[0].text # product_name
                        date = element.find_elements_by_xpath(DATE_XPATH)[0].text # date
                        star = element.find_elements_by_xpath(
                            STAR_XPATH)[0].get_attribute('data-rating') # Score

                        try:
                            headline = element.find_elements_by_class_name(
                                HEADLINE_CLASS_NAME)[0].text # headline
                        except:
                            headline = ''

                        try:
                            content = element.find_elements_by_class_name(
                                CONTENT_CLASS_NAME)[0].text # content
                        except:
                            content =  ''

                        # append result                   
                        tmp = pd.DataFrame({'writer':[name], 
                                            'score':[star], 
                                            'data':[date], 
                                            'product_name':[product], 
                                            'headline':[headline], 
                                            'content':[content], 
                                            'url':[url], 
                                            'rank':[url_idx+1], 
                                            'search_keyword':[keyword]}) 
                        result = result.append(tmp, ignore_index=True)

                    # Reset page_value
                    if page_value == 13:
                        page_value = 3

                    # Move page
                    location_area=driver.find_element_by_xpath(page_move_xpath.format(page_value))
                    driver.execute_script(f"window.scrollTo(0, {location_area.location['y']-200})") 
                    time.sleep(1)
                    location_area.click()
                    time.sleep(2)

                    # page += 1
                    page_value += 1

                except: 
                    break 

            # If while loop is break, Click another score's review
            driver.execute_script(f"window.scrollTo(0, {location2.location['y']-300})") 
            time.sleep(2)
            driver.find_element_by_xpath(MOVE_XPATH5).click()

        # url complete log
        # print(f'== {url_idx}번째 완료 == 경과시간: {round(time.time()-t1)}초')
        driver.close()

        # save (per library)
        if url_idx == (df_url.shape[0]-1):
            os.makedirs(f'{detaildata_save_path.format(library)}', exist_ok=True)
            dstpath = f'{detaildata_save_path.format(library)}/{library}(detail).csv'
            result.to_csv(dstpath, index=False, encoding='utf-8-sig')
            result_final = result_final.append(result, ignore_index=True)

        else:
            if df_url.loc[url_idx, 'library'] != df_url.loc[url_idx+1, 'library']:
                os.makedirs(f'{detaildata_save_path.format(library)}', exist_ok=True)
                dstpath = f'{detaildata_save_path.format(library)}/{library}(detail).csv'
                result.to_csv(dstpath, index=False, encoding='utf-8-sig')
                result_final = result_final.append(result, ignore_index=True)
                result = pd.DataFrame()

    return result_final
