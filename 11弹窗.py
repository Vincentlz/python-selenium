from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(15)
driver.get('http://cdn1.python3.vip/files/selenium/test4.html')

# 获取网站标题栏文本
print(driver.title)

# 获取网站地址栏文本
print(driver.current_url)

# 截屏保存为图片文件
driver.get_screenshot_as_file('1.png')

# --- alert ---
driver.find_element(By.ID, 'b1').click()

# 打印 弹出框 提示信息
print(driver.switch_to.alert.text)

# 点击 OK 按钮
driver.switch_to.alert.accept()

# --- confirm ---
driver.find_element(By.ID, 'b2').click()

# 打印 弹出框 提示信息
print(driver.switch_to.alert.text)

# 点击 OK 按钮
driver.switch_to.alert.accept()

driver.find_element(By.ID, 'b2').click()

# 点击 取消 按钮
driver.switch_to.alert.dismiss()

# --- prompt ---
driver.find_element(By.ID, 'b3').click()

# 获取 alert 对象
alert = driver.switch_to.alert

# 打印 弹出框 提示信息
print(alert.text)

# 输入信息，并且点击 OK 按钮 提交
alert.send_keys('web自动化 - selenium')
alert.accept()

# 点击 Cancel 按钮 取消
driver.find_element(By.ID, 'b3').click()
alert = driver.switch_to.alert
alert.dismiss()

driver.close()
