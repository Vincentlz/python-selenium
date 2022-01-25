from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# 下拉框的操作相对复杂一些，需要用到Select模块
from selenium.webdriver.support.select import Select

url = 'D:\myworker\pycode\seleniumcode\下拉框.html'

browser = webdriver.Chrome()
browser.get(url)
time.sleep(3)

# browser.get(r'https://www.baidu.com')
'''
# 输入文本
# 定位搜索框
# input = browser.find_element_by_class_name('s_ipt')
# # 输入python
# input.send_keys('python')

# # 点击
# # 选中新闻按钮
# click = browser.find_element_by_link_text('新闻')
# # 点击之
# click.click()

# # 清除文本
# # 定位搜索框
# input = browser.find_element_by_class_name('s_ipt')
# # 输入python
# input.send_keys('python')
# time.sleep(2)
# # 清除python
# input.clear()

# # 回车确认
# # 定位搜索框
# input = browser.find_element_by_class_name('s_ipt')
# # 输入python
# input.send_keys('python')
# time.sleep(2)
# # 回车查询
# input.submit()
'''
'''
# 1、三种选择某一选项项的方法

select_by_index()           # 通过索引定位；注意：index索引是从“0”开始。
select_by_value()           # 通过value值定位，value标签的属性值。
select_by_visible_text()    # 通过文本值定位，即显示在下拉框的值。

# 2、三种返回options信息的方法

options                     # 返回select元素所有的options
all_selected_options        # 返回select元素中所有已选中的选项
first_selected_options      # 返回select元素中选中的第一个选项                  


# 3、四种取消选中项的方法

deselect_all                # 取消全部的已选择项
deselect_by_index           # 取消已选中的索引项
deselect_by_value           # 取消已选中的value值
deselect_by_visible_text    # 取消已选中的文本值
'''
# 单选

# 多选

# 下拉框
# 根据索引选择
Select(browser.find_element(By.NAME, "帅哥")).select_by_index("2")
time.sleep(2)
# 根据value值选择
Select(browser.find_element(By.NAME, "帅哥")).select_by_value("草儿")
time.sleep(2)
# 根据文本值选择
Select(browser.find_element(By.NAME, "帅哥")).select_by_visible_text("才哥")
time.sleep(2)

# 关闭浏览器
browser.close()
