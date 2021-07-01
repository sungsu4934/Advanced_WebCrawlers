# Advanced WebCrawler (lxml & selenium)

### 구성내용
 - 쿠팡 웹페이지에 특정 키워드를 검색하고 상위 리뷰순으로 정렬한 후 상위 10개의 품목에 대해서만 리뷰를 수집
 - 웹 크롤링 도구를 모듈화 및 패키지화하여 더욱 전문성있게 구성 (.py 파일)
 - Code Convention 실시
 - 진행방식
  > 1) 세부정보가 담긴 url을 우선적으로 크롤링
  > 2) 세부정보 크롤링

### Input 데이터 형태
 - library: keywords 의 형태로 구성되어 있음. (resource/sample_data.xlsx 참조)
 - 예시: {과일:[수박, 토마토, 사과, 포도], 컴퓨터: [본체, 마우스, 프린터, 키보드]}

### 폴더 구성
 - conf: 크롤링을 위한 xpath 등의 파라미터
  > 1) coupang_urlcrawl_parameter.py: url 크롤링을 위한 파라미터
  > 2) coupang_detailcrawl_parameter.py: 세부정보 크롤링을 위한 파라미터
  
 - data: 크롤링 완료된 데이터 및 크롤링 오류 로그
  > 1) crawling_data: 라이브러리별로 1차 구분, url 크롤링 값인지 세부정보 크롤링 값인지 2차 구분
  > 2) logs: 라이브러리별로 1차 구분, 오류 발생 날짜로 2차 구분, url 크롤링 값인지 세부정보 크롤링 값인지 3차 구분

 - resource: chromedriver 등 크롤링에 필요한 도구들

 - src: 크롤링 및 logging 프로세스
  > 1) coupang_urlcrawl.py: url 정보 크롤링 프로세스
  > 2) coupang_detailcrawl.py: 세부정보 크롤링 프로세스
  > 3) utils - logging.py: log를 기록하기 위한 프로세스

### log & save_data
 - 오류가 발생할 때 마다 현재시각 및 오류 내용을 기입 (logging.py)
 - 라이브러리가 종료될 때 마다 중간저장

### 포함된 웹
 - 쿠팡
