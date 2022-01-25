# 这节我们就从初始化浏览器对象、访问页面、设置浏览器大小、刷新页面和前进后退等基础操作。

from selenium import webdriver
import time
# 初始化浏览器为Chrome浏览器
browser = webdriver.Chrome()

# 指定绝对路径的方式
# path = r'C:\Users\Gdc\.wdm\drivers\chromedriver\win32\96.0.4664.45\chromedriver.exe'

# 无界面的浏览器
# option = webdriver.ChromeOptions()
# option.add_argument("headless")

# 等待
browser.implicitly_wait(300)

# 设置浏览器大小，全屏
browser.maximize_window()
time.sleep(3)
print('全屏了')
# 设置分辨率500*500
# browser.set_window_size(500, 500)
# time.sleep(3)

# 设置分辨率1000*1000
# browser.set_window_size(1000, 1000)
# time.sleep(3)

# 打开浏览器
# browser = webdriver.Chrome(options=option) #无界
browser = webdriver.Chrome()

# 访问百度首页
browser.get('https://www.baidu.com/')
print('打开百度')

# 打开淘宝页面
browser.get('https://www.taobao.com/')
print('打开淘宝')

# 后退到百度页面
browser.back()
time.sleep(3)
print('后退百度')

# 前进到淘宝页面
browser.forward()
time.sleep(3)
print('前进淘宝')

# 刷新页面
try:
    browser.refresh()
    print('刷新页面')
except Exception:
    print('刷新失败')

# 截图预览
browser.get_screenshot_as_file('百度截图.png')
print('截图成功！')

# 关闭浏览器
time.sleep(3)
browser.close()
