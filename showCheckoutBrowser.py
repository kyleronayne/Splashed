import time
from bs4 import BeautifulSoup as bs
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

def getCart(taskData, splashBrowser):
    cartUrls = {'au': 'https://www.adidas.com.au/on/demandware.store/Sites-adidas-AU-Site/en_AU/Cart-Show',
                'uk': 'https://www.adidas.co.uk/on/demandware.store/Sites-adidas-GB-Site/en_GB/Cart-Show',
                'fr': 'https://www.adidas.fr/on/demandware.store/Sites-adidas-FR-Site/fr_FR/Cart-Show',
                'ca': 'https://www.adidas.ca/on/demandware.store/Sites-adidas-CA-Site/en_CA/Cart-Show',
                'us': 'https://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/Cart-Show'}
    for urlRegion in cartUrls:
        if urlRegion == taskData['region']:
            cartUrl = cartUrls[urlRegion]
    splashBrowser.execute_script("window.open('" + cartUrl + "', 'new window')")
    openTabs = splashBrowser.window_handles
    splashBrowser.switch_to.window(openTabs[0])

def getSitekey(splashBrowser, taskData):
    productPageSoup = bs(splashBrowser.page_source, 'html.parser')
    try:
        sitekey = productPageSoup.find('div', {'class': 'g-recaptcha'}).get('data-sitekey')
        taskData['sitekey'] = sitekey
    except:
        taskData['sitekey'] = 'N/A'

def successNotification(taskData):
    print(time.strftime('[%I:%M:%S %p - Task ' + str(taskData['taskNumber']) + '] ') + 'Past Splash! Launching Checkout Browser')
    print(time.strftime('[%I:%M:%S %p - Task ' + str(taskData['taskNumber']) + '] ') + 'Task Data: ' + str(taskData))

def showBrowser(splashBrowser, config):
    cookies = splashBrowser.get_cookies()
    splashBrowser.quit()
    driverOptions = Options()
    driverOptions.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
    driverOptions.add_argument('disable-infobars')
    checkoutBrowser = webdriver.Chrome(chrome_options = driverOptions)
    checkoutBrowser.get(config['splashUrl'])
    for cookie in cookies:
        checkoutBrowser.add_cookie(cookie)
    checkoutBrowser.refresh()

def stayAlive():
    while True:
        None

def showChekoutBrowser(splashBrowser, taskData, config):
    getCart(taskData, splashBrowser)
    getSitekey(splashBrowser, taskData)
    successNotification(taskData)
    showBrowser(splashBrowser, config)
    stayAlive()
