from selenium import webdriver
from selenium.webdriver.common.by import By

# get_attribute获取属性

browser = webdriver.Chrome()

browser.get('https://www.baidu.com')

# 获取logo图片地址
logo = browser.find_element(By.CLASS_NAME, 'index-logo-src')

print(logo)

print('图片链接：' + logo.get_attribute('src'))


# 获取文本
logo_text = browser.find_element(By.CSS_SELECTOR, '#hotsearch-content-wrapper > li:nth-child(1) > a')

print(logo_text.text)

print('文本内容：' + logo_text.get_attribute('href'))

# 还有id、位置、标签名和大小等属性
logo = browser.find_element(By.CLASS_NAME, 'index-logo-src')
print(logo.id)
print(logo.location)
print(logo.tag_name)
print(logo.size)

# 关闭浏览器
browser.close()
