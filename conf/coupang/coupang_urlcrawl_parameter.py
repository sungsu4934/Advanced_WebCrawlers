LIBRARY_PATH = 'resource/sample_data.xlsx'

"""
LIBRARY_PATH: path for Library which KOTITI gives to you 
"""

USERAGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
HEADERS = {'User-Agent' : USERAGENT}

"""
USERAGENT, HEADERS: lxml's option. You can use your useragent or fake-useragent
"""

urlcrawl_baseurl = 'https://www.coupang.com/np/search?rocketAll=false&q={}&brand=&offerCondition=&filter=&availableDeliveryFilter=&filterType=&isPriceRange=false&priceRange=&minPrice=&maxPrice=&page=1&trcid=&traid=&filterSetByUser=true&channel=user&backgroundColor=&component=&rating=0&sorter=saleCountDesc&listSize=36'
URLCRAWL_URL_XPATH = '/html/body/div[2]/section/form/div[2]/div[2]/ul/li'
URLCRAWL_PRODUCT_XPATH = '//a/dl/dd/div/div[2]'
urlcrawl_review_num_xpath = '/html/body/div[2]/section/form/div[2]/div[2]/ul/li[{}]/a/dl/dd/div/div[4]/div/span[2]'

"""
urlcrawl_baseurl: base url for url crawling
URLCRAWL_URL_XPATH: xpath for detail webpage's url
URLCRAWL_PRODUCT_XPATH: xpath for product name
urlcrawl_review_num_xpath: xpath for how many review's the product has
"""

urldata_save_path = 'data/crawling_data/coupang/{}'
urldata_log_path = 'data/logs/coupang/{}'

"""
urldata_save_path: save path for url crawling temporary csv
urldata_log_path: save path for url crawling log
"""