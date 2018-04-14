import time
from bs4 import BeautifulSoup as bs
from selenium.webdriver.firefox.options import Options
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
    checkoutBrowserProfile = webdriver.FirefoxProfile()
    checkoutBrowserProfile.set_preference('general.useragent.override', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0')
    checkoutBrowserOptions = Options()
    checkoutBrowserOptions.add_argument('--disable-extensions')
    checkoutBrowserOptions.add_argument('--disable-infobars')
    checkoutBrowser = webdriver.Firefox(checkoutBrowserProfile, firefox_options = checkoutBrowserOptions)
    checkoutBrowser.delete_all_cookies()
    checkoutBrowser.set_window_position(600, 0)
    return checkoutBrowser

def addCookies(checkoutBrowser, config, gmailCookies, productPageCookies):
    checkoutBrowser.get('https://www.google.com/')
    for cookie in gmailCookies:
        checkoutBrowser.add_cookie(cookie)
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

def showCheckoutBrowser(splashBrowser, taskData, config, gmailCookies):
    productPageCookies = getProductPageCookies(splashBrowser)
    #getCart(taskData, splashBrowser)
    checkoutBrowser = launchCheckoutBrowser(splashBrowser, config)
    addCookies(checkoutBrowser, config, gmailCookies, productPageCookies)
    getSitekey(checkoutBrowser, taskData)
