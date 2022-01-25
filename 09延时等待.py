from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

# 强制等待 直接time.sleep(n)强制等待n秒，在执行get方法之后执行

# 隐式等待 implicitly_wait()设置等待时间，如果到时间有元素节点没有加载出来，就会抛出异常
# 隐式等待，等待时间10秒
browser.implicitly_wait(10)

browser.get('https://www.baidu.com')
print(browser.current_url)
print(browser.title)

browser.close()

# 显示等待
'''设置一个等待时间和一个条件，在规定时间内，每隔一段时间查看下条件是否成立，如果成立那么程序就继续执行，否则就抛出一个超时异常。'''

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
# 设置等待时间10s
wait = WebDriverWait(browser, 10)
# 设置判断条件：等待id='kw'的元素加载完成
input = wait.until(EC.presence_of_element_located((By.ID, 'kw')))
# 在关键词输入：关键词
input.send_keys('Python')

# 关闭浏览器
time.sleep(2)
browser.close()
'''
WebDriverWait(driver,timeout,poll_frequency=0.5,ignored_exceptions=None)

driver: 浏览器驱动

timeout: 超时时间，等待的最长时间（同时要考虑隐性等待时间）

poll_frequency: 每次检测的间隔时间，默认是0.5秒

ignored_exceptions:超时后的异常信息，默认情况下抛出NoSuchElementException异常

until(method,message='')

method: 在等待期间，每隔一段时间调用这个传入的方法，直到返回值不是False

message: 如果超时，抛出TimeoutException，将message传入异常

until_not(method,message='')

until_not 与until相反，until是当某元素出现或什么条件成立则继续执行，until_not是当某元素消失或什么条件不成立则继续执行，参数也相同。
'''

# 其他等待条件

'''
from selenium.webdriver.support import expected_conditions as EC
# 判断标题是否和预期的一致
title_is
# 判断标题中是否包含预期的字符串
title_contains

# 判断指定元素是否加载出来
presence_of_element_located
# 判断所有元素是否加载完成
presence_of_all_elements_located

# 判断某个元素是否可见. 可见代表元素非隐藏，并且元素的宽和高都不等于0，传入参数是元组类型的locator
visibility_of_element_located
# 判断元素是否可见，传入参数是定位后的元素WebElement
visibility_of
# 判断某个元素是否不可见，或是否不存在于DOM树
invisibility_of_element_located

# 判断元素的 text 是否包含预期字符串
text_to_be_present_in_element
# 判断元素的 value 是否包含预期字符串
text_to_be_present_in_element_value

#判断frame是否可切入，可传入locator元组或者直接传入定位方式：id、name、index或WebElement
frame_to_be_available_and_switch_to_it

#判断是否有alert出现
alert_is_present

#判断元素是否可点击
element_to_be_clickable

# 判断元素是否被选中,一般用在下拉列表，传入WebElement对象
element_to_be_selected
# 判断元素是否被选中
element_located_to_be_selected
# 判断元素的选中状态是否和预期一致，传入参数：定位后的元素，相等返回True，否则返回False
element_selection_state_to_be
# 判断元素的选中状态是否和预期一致，传入参数：元素的定位，相等返回True，否则返回False
element_located_selection_state_to_be

#判断一个元素是否仍在DOM中，传入WebElement对象，可以判断页面是否刷新了
staleness_of
'''
