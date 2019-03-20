## 1.安装不同浏览器的driver
Chrome:
https://sites.google.com/a/chromium.org/chromedriver/downloads
chromedriver.exe

Edge:
https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
MicrosoftWebDriver.exe

Firefox:
https://github.com/mozilla/geckodriver/releases
geckodriver.exe

Safari:
https://webkit.org/blog/6900/webdriver-support-in-safari-10/

IE:
http://selenium-release.storage.googleapis.com/index.html
IEDriverServer.exe

参考：https://pypi.org/project/selenium/


## 2.把driver文件放在python的安装目录下

比如如果需要启动firefox则把geckodriver.exe放到C:\Users\lucy.liuh\AppData\Local\Programs\Python\Python35
同理其他


## 3.python调用selenium启动浏览器

3.1 启动firefox

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

3.2 启动IE

from selenium import webdriver

driver = webdriver.Ie()
driver.get("https://www.baidu.com")

3.3 启动chrome

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

3.4 启动edge

遇到问题：urllib3.exceptions.ProtocolError: ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))

原因：下载的driver的版本和安装的edge浏览器的版本不兼容



from selenium import webdriver

driver = webdriver.Edge()
driver.get("https://www.baidu.com")
# Selenium-Browser
support different browsers
