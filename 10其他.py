from selenium import webdriver
import time

browser = webdriver.Chrome()
# 知乎发现页
browser.get('https://www.zhihu.com/explore')

# 还有一些操作，比如下拉进度条，模拟javaScript，使用execute_script方法来实现
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')
time.sleep(15)

# 在selenium使用过程中，还可以很方便对Cookie进行获取、添加与删除等操作
# 知乎发现页
browser.get('https://www.zhihu.com/explore')
# 获取cookie
print(f'Cookies的值：{browser.get_cookies()}')
# 添加cookie
browser.add_cookie({'name': '才哥', 'value': '帅哥'})
print(f'添加后Cookies的值：{browser.get_cookies()}')
# 删除cookie
browser.delete_all_cookies()
print(f'删除后Cookies的值：{browser.get_cookies()}')
