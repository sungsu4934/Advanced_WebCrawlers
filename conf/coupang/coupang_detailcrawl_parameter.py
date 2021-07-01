from selenium.webdriver.chrome.options import Options

# selenium option
SELENIUM_OPTION = Options()
SELENIUM_OPTION.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

"""
SELENIUM OPTIONS: options for selenium crawling. You can add options which you want
"""

# path for chrome.exe, chromedriver.exe
CHROME_EXE_PATH = r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"'
CHROMEDRIVER_PATH = 'resource/chromedriver_91.exe'

"""
CHROME_EXE_PATH: For coupang webpage, you need to approach to webpage using chrome.exe. Without it, you can't access
CHROMEDRIVER_PATH: Chromedriver path for selenium
"""

# XPATHS to access reviews
MOVE_XPATH1 = '//*[@id="itemBrief"]/div/p[1]' # 필수 표기정보
MOVE_XPATH2 = '//*[@id="btfTab"]/ul[1]/li[2]' # 상품평
MOVE_XPATH3 = '//*[@id="btfTab"]/ul[2]/li[2]/div/div[5]/section[2]/div[1]' # 별점보기 칸
MOVE_XPATH4 = '//*[@id="btfTab"]/ul[2]/li[2]/div/div[5]/section[2]/div[3]/div[1]/div[1]/img[2]' # 별점보기
MOVE_XPATH5 = '//*[@id="btfTab"]/ul[2]/li[2]/div/div[5]/section[2]/div[3]/div[1]'
"""
MOVE_XPATH 1~5: XPATHS to access reviews
"""

# Scores' Xpath
MOTION1_XPATH = '//*[@id="btfTab"]/ul[2]/li[2]/div/div[5]/section[2]/div[3]/div[2]/ul/li[5]' # Score: 1
MOTION2_XPATH = '//*[@id="btfTab"]/ul[2]/li[2]/div/div[5]/section[2]/div[3]/div[2]/ul/li[4]' # Score: 2
MOTION3_XPATH = '//*[@id="btfTab"]/ul[2]/li[2]/div/div[5]/section[2]/div[3]/div[2]/ul/li[3]' # Score: 3

"""
MOTION1~3_XPATH: Xpath for Review score between 1~3
"""

# detail information's xpath
ELEMENTS_XPATH = '//*[@id="btfTab"]/ul[2]/li[2]/div/div[5]/section[4]/article'
NAME_XPATH = 'div[1]/div[2]/span' # writer
PRODUCT_XPATH = 'div[1]/div[4]' # product_name
DATE_XPATH = 'div[1]/div[3]/div[2]' # date
STAR_XPATH = 'div[1]/div[3]/div[1]/div' # score
HEADLINE_CLASS_NAME = 'sdp-review__article__list__headline' # headline
CONTENT_CLASS_NAME = 'js_reviewArticleContent' # content

"""
ELEMENTS_XPATH, ..., CONTENT_CLASS_NAME: Each Information's Xpath
"""

# page bar
page_move_xpath = '//*[@id="btfTab"]/ul[2]/li[2]/div/div[5]/section[4]/div[3]/button[{}]'

"""
page_move_xpath: Xpath for page bar
"""
            
# save path
detaildata_save_path = 'data/crawling_data/coupang/{}'
detaildata_log_path = 'data/logs/coupang/{}'

"""
detaildata_save_path: save path for detail crawling temporary csv
detaildata_log_path: save path for detail crawling log
"""