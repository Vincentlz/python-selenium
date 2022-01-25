# 当我们用selenium打开某个页面，有一些基础属性如网页标题、网址、浏览器名称、页面源码等信息。

from selenium import webdriver

browser = webdriver.Chrome()
browser.get(r'https://www.baidu.com')

# 网页标题
print(browser.title)
# 当前网址
print(browser.current_url)
# 浏览器名称
print(browser.name)
# 网页源码
print(browser.page_source)

# 需要注意的是，这里的页面源码我们就可以用正则表达式、Bs4、xpath以及pyquery等工具进行解析提取想要的信息了。
