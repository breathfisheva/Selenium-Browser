from  selenium import webdriver

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

for broswer in browsers:
    driver = init_webdriver(broswer)
    driver.get('https://www.baidu.com')
    driver.close()
