# 模拟鼠标的类
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 左键，就是点击 click()操作

# 右键 context_click()

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
time.sleep(3)

# 定位到要右击的元素，这里选择新闻链接
right_click = browser.find_element(By.LINK_TEXT, '新闻')

'''ActionChains(browser)：调用ActionChains()类，并将浏览器驱动browser作为参数传入

context_click(right_click)：模拟鼠标双击，需要传入指定元素定位作为参数

perform()：执行ActionChains()中储存的所有操作，可以看做是执行之前一系列的操作'''
# 执行右键操作
ActionChains(browser).context_click(right_click).perform()
time.sleep(3)


# 双击 double_click()
# 定位到双击的元素
double_click = browser.find_element(By.CSS_SELECTOR, '#bottom_layer > div > p:nth-child(8) > span')

# 双击
ActionChains(browser).double_click(double_click).perform()
time.sleep(3)


# 拖拽 drag_and_drop(source,target)开始位置和结束位置需要被指定，这个常用于滑块类验证码的操作之类
url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)  
time.sleep(2)

browser.switch_to.frame('iframeResult')

# 开始位置
source = browser.find_element(By.CSS_SELECTOR, '#draggable')

# 结束位置
target = browser.find_element(By.CSS_SELECTOR, '#droppable')

# 执行元素的拖拽操作
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()
# 拖拽
time.sleep(15)


# 悬停 move_to_element()
url = 'https://www.baidu.com'
browser.get(url)  
time.sleep(2)

# 定位悬停的位置
move = browser.find_element(By.CSS_SELECTOR, "#form > span.bg.s_ipt_wr.new-pmd.quickdelete-wrap > span.soutu-btn")

# 悬停操作
ActionChains(browser).move_to_element(move).perform()
time.sleep(5)

# 关闭浏览器
browser.close()
