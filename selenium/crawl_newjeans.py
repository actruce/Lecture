# 셀레니움 웹 드라이버 임포트 해 주기
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Chrome 브라우저 열기
browser = webdriver.Chrome()

# 구글 페이지 연결시키기
url = "file:///F:/Downloads/NewJeans.html"

#go to board
try:
    browser.get(url)
  
except:
    print("ERROR while entering webpage")

print('\n\n')

# element.text
element = browser.find_element(By.TAG_NAME, 'h1')
h1_txt = element.text
print(h1_txt)

print('\n\n')

# element.get_attribute
element = browser.find_element(By.TAG_NAME, 'img')
img_src = element.get_attribute('src')
print(img_src)

print('\n\n')

# elements
elements = browser.find_elements(By.TAG_NAME, 'ul')
for elem in elements:
    print(elem.text)

print('\n\n')

# find_element + find_elements
hot100 = browser.find_element(By.ID, 'table_h100')
elements = hot100.find_elements(By.TAG_NAME, 'tr')
for elem in elements:
    print(elem.text)


time.sleep(10)    


browser.quit()