import time
from bs4 import BeautifulSoup as bs
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

def getProductPageCookies(splashBrowser):
    productPageCookies = splashBrowser.get_cookies()
    splashBrowser.quit()
    return productPageCookies

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

def launchCheckoutBrowser(splashBrowser, config):
    checkoutBrowserOptions = Options()
    checkoutBrowserOptions.add_argument('disable-infobars')
    checkoutBrowserOptions.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
    checkoutBrowserOptions.add_argument('Accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8')
    checkoutBrowserOptions.add_argument('Accept-Encoding=gzip, deflate, br')
    checkoutBrowserOptions.add_argument('Accept-Language=en-US,en;q=0.9')
    #checkoutBrowserOptions.add_argument('Host=www.adidas.com')
    checkoutBrowserOptions.add_argument('Referer=' + config['splashUrl'])
    checkoutBrowserOptions.add_argument('Upgrade-Insecure-Requests=1')
    checkoutBrowser = webdriver.Chrome(chrome_options = checkoutBrowserOptions)
    return checkoutBrowser

def addProductPageCookies(checkoutBrowser, config, productPageCookies):
    checkoutBrowser.get(config['splashUrl'])
    for cookie in productPageCookies:
        checkoutBrowser.add_cookie(cookie)
    checkoutBrowser.refresh()

def getSitekey(checkoutBrowser, taskData):
    productPageSoup = bs(checkoutBrowser.page_source, 'html.parser')
    try:
        sitekey = productPageSoup.find('div', {'class': 'g-recaptcha'}).get('data-sitekey')
        taskData['sitekey'] = sitekey
    except:
        taskData['sitekey'] = 'N/A'

def showCheckoutBrowser(splashBrowser, taskData, config):
    productPageCookies = getProductPageCookies(splashBrowser)
    #getCart(taskData, splashBrowser)
    checkoutBrowser = launchCheckoutBrowser(splashBrowser, config)
    addProductPageCookies(checkoutBrowser, config, productPageCookies)
    getSitekey(checkoutBrowser, taskData)
