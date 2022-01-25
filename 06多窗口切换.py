# elenium打开一个页面之后，默认是在父页面进行操作，此时如果这个页面还有子页面，想要获取子页面的节点元素信息则需要切换到子页面进行擦走，这时候switch_to.frame()就来了。如果想回到父页面，用switch_to.parent_frame()即可

# 选项卡切换
# current_window_handle：获取当前窗口的句柄。

# window_handles：返回当前浏览器的所有窗口的句柄。

# switch_to_window()：用于切换到对应的窗口。

from selenium import webdriver
import time

browser = webdriver.Chrome()

# 打开百度
browser.get('http://www.baidu.com')
# 新建一个选项卡
browser.execute_script('window.open()')
print(browser.window_handles)
# 跳转到第二个选项卡并打开知乎
browser.switch_to.window(browser.window_handles[1])
browser.get('http://www.zhihu.com')
# 回到第一个选项卡并打开淘宝（原来的百度页面改为了淘宝）
time.sleep(2)
browser.switch_to.window(browser.window_handles[0])
browser.get('http://www.taobao.com')
