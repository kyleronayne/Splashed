from bs4 import BeautifulSoup as bs
import random
import time

def getPageSoup(splashBrowser):
    pageSoup = bs(splashBrowser.page_source, 'html.parser')
    return pageSoup

def checkConnection(pageSoup, taskData, splashBrowser):
    for errorString in ['unfortunately we are unable to give you access to our site at this time. ', 'this page isn’t working', 'proxy error']:
        if errorString in pageSoup.text.lower():
            print(time.strftime('[%I:%M:%S %p - Task ' + str(taskData['taskNumber']) + '] ') + 'Connection Error, Reloading Splash Page!')
            splashBrowser.refresh()
            break

def detector1(pageSoup):
    try:
        if pageSoup.find('button', text = 'Add To Bag'):
            productPage = True
            return productPage
    except:
        None

def detector2(pageSoup):
    try:
        if pageSoup.find('div', {'data-auto-id': 'size-selector'}):
            productPage = True
            return productPage
    except:
        None

def detector3(pageSoup):
    try:
        if pageSoup.find('div', {'id': 'g-recaptcha'}):
            productPage = True
            return productPage
    except:
        None

def customDetector(splashBrowser):
    configFile = eval(open('config.txt', 'r').read())
    customDetector = configFile['customDetector']
    if customDetector:
        try:
            splashBrowser.find_element_by_css_selector(customDetector)
            productPage = True
            return productPage
        except:
            None

def pageInteraction(splashBrowser):
    try:
        splashBrowser.find_element_by_class_name('inner').click()
    except:
        None

def productDetection(splashBrowser, taskData):
    while True:
        pageSoup = getPageSoup(splashBrowser)
        checkConnection(pageSoup, taskData, splashBrowser)
        productPage = detector1(pageSoup)
        if productPage:
            break
        productPage = detector2(pageSoup)
        if productPage:
            break
        productPage = detector3(pageSoup)
        if productPage:
            break
        productPage = customDetector(pageSoup)
        if productPage:
            break
        pageInteraction(splashBrowser)
        detectionDelay = random.randint(60, 120)
        time.sleep(detectionDelay)
