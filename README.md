# Advanced WebCrawler (lxml & selenium)

## 구성내용
 - 웹 크롤링 도구를 모듈화 및 패키지화하여 더욱 전문성있게 구성
 - Code Convention 실시
 - 진행방식
  > 1) 세부 정보가 담긴 url을 우선적으로 크롤링 한 후 
  > 2) 세부정보 크롤링

## 웹크롤러 구성
 - parameter.py: 각 구성요소별 xpath 등 파라미터 표기
 - urlc_crawler.py: url을 크롤링하는 로직
 - detailc_crawler.py: detail을 크롤링하는 로직

## log & save_data
 - 오류가 발생할 때 마다 현재시각 및 오류 내용을 기입 (logging.py)
 - 라이브러리가 종료될 때 마다 중간저장

## 포함된 웹
 - 네이버 카페 게시글 크롤링
 - 쿠팡 쇼핑몰 리뷰 크롤링

## Input 데이터 형태
 - 
