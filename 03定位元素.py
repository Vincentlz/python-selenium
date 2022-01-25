# <input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off">

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

browser.get(r'https://www.baidu.com')
time.sleep(2)

# 在搜索框输入 python
# browser.find_element_by_id('kw').send_keys('python')
browser.find_element(By.ID, 'kw').send_keys('python')

browser.find_element(By.NAME, 'wd').send_keys('python')

browser.find_element(By.CLASS_NAME, 's_ipt').send_keys('python')

# 存在多个input会报错
browser.find_element(By.TAG_NAME, 'input').send_keys('python')

browser.find_element(By.LINK_TEXT, '新闻').click()

browser.find_element(By.PARTIAL_LINK_TEXT, '闻').click()

browser.find_element(By.XPATH, '//*[@id="kw"]').send_keys('python')

browser.find_element(By.CSS_SELECTOR, '#kw').send_keys('python')

time.sleep(2)

# 关闭浏览器
browser.close()
