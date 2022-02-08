from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(15)
driver.get('http://cdn1.python3.vip/files/selenium/test1.html')

# 先寻找id是china的元素
china = driver.find_element(By.ID, 'china')

# 再选择该元素内部的p元素
elements = china.find_elements(By.XPATH, './/p')

# 打印结果
for element in elements:
    print('----------------')
    print(element.get_attribute('outerHTML'))


multi = driver.find_element(By.CLASS_NAME, 'multi_choice')

multichoice = multi.find_elements(By.XPATH, './/option')

for element in multichoice:
    print('----------------')
    print(element.get_attribute('outerHTML'))


# 先寻找id是us的元素
china = driver.find_element(By.ID, 'us')

# 再选择该元素内部的p元素
elements = china.find_elements(By.XPATH, './/p')

# 打印结果
for element in elements:
    print('----------------')
    print(element.get_attribute('outerHTML'))
