'''
使用协程实现异步
'''

from  selenium import webdriver
import asyncio

browsers = ['Firefox', 'Chrome', 'IE', 'Edge']

def init_webdriver(broswer):
    if broswer == 'Firefox':
        return webdriver.Firefox()
    elif broswer == 'Chrome':
        return webdriver.Chrome()
    elif broswer == 'IE':
        return  webdriver.Ie()
    elif broswer == 'Edge':
        return webdriver.Edge()

@asyncio.coroutine
def visi_website(broswer):
    driver = init_webdriver(broswer)
    yield from asyncio.sleep(1) #必须用异步，否则即使用了coroutine也没法实现异步
    driver.get('https://www.baidu.com')
    driver.close()

loop = asyncio.get_event_loop()
tasks = []
for browser in browsers:
    tasks.append(visi_website(browser))
print(tasks)
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

