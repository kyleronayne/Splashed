import time
from bs4 import BeautifulSoup as bs

def successNotification(taskData):
    print(time.strftime('[%I:%M:%S %p - Task ' + str(taskData['taskNumber']) + '] ') + 'Past Splash!')

def getSitekey(splashBrowser, taskData):
    productPageSoup = bs(splashBrowser.page_source, 'html.parser')
    try:
        sitekey = productPageSoup.find('div', {'class': 'g-recaptcha'}).get('data-sitekey')
        print(time.strftime('[%I:%M:%S %p - Task ' + str(taskData['taskNumber']) + '] ') + 'Sitekey: ' + sitekey)
    except:
        print(time.strftime('[%I:%M:%S %p - Task ' + str(taskData['taskNumber']) + '] ') + 'Unable To Get Sitekey!')

def getCart(taskData, splashBrowser):
    print(time.strftime('[%I:%M:%S %p - Task ' + str(taskData['taskNumber']) + '] ') + 'Inject ATC Code Or Manually Add To Cart!')
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

def showBrowser(splashBrowser):
    splashBrowser.maximize_window()

def stayAlive():
    while True:
        None

def showSplashBrowser(splashBrowser, taskData):
    successNotification(taskData)
    getSitekey(splashBrowser, taskData)
    getCart(taskData, splashBrowser)
    showBrowser(splashBrowser)
    stayAlive()
