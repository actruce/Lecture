# 셀레니움 웹 드라이버 임포트 해 주기
from selenium import webdriver

# Chrome 브라우저 열기
driver = webdriver.Chrome()

# 구글 페이지 연결시키기
browser = driver.get("https://google.com")

# 창을 종료할 때까지 계속 떠있게 하기
while True:
    pass

# 웹 페이지 종료
driver.quit()