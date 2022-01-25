from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

'''
send_keys(Keys.BACK_SPACE)：删除键(BackSpace)

send_keys(Keys.SPACE)：空格键(Space)

send_keys(Keys.TAB)：制表键(TAB)

send_keys(Keys.ESCAPE)：回退键(ESCAPE)

send_keys(Keys.ENTER)：回车键(ENTER)

send_keys(Keys.CONTRL,'a')：全选(Ctrl+A)

send_keys(Keys.CONTRL,'c')：复制(Ctrl+C)

send_keys(Keys.CONTRL,'x')：剪切(Ctrl+X)

send_keys(Keys.CONTRL,'v')：粘贴(Ctrl+V)

send_keys(Keys.F1)：键盘F1

.....

send_keys(Keys.F12)：键盘F12
'''

browser = webdriver.Chrome()
url = 'https://www.baidu.com'
browser.get(url)
time.sleep(2)

# 定位搜索框
input = browser.find_element(By.CLASS_NAME, 's_ipt')
# 输入python
input.send_keys('python')
time.sleep(2)

# 回车
input.send_keys(Keys.ENTER)
time.sleep(5)

# 关闭浏览器
browser.close()
