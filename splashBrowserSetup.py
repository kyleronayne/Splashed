import random
from selenium.webdriver import DesiredCapabilities
import zipfile
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import time


def launchSplashBrowser(taskData, proxyPlugin):
    driverOptions = dict(DesiredCapabilities.PHANTOMJS)
    driverOptions['phantomjs.page.settings.userAgent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
    driverOptions['phantomjs.page.customHeaders'] = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                                                    #'Accept-Encoding': 'gzip, deflate, br',
                                                    'Accept-Language': 'en-US,en;q=0.9',
                                                    'Connection': 'keep-alive',
                                                    #'Host': 'www.adidas.com',
                                                    'Referer': 'https://www.adidas.com/us',
                                                    'Upgrade-Insecure-Requests': '1',
                                                    'Content-Type': 'application/x-www-form-urlencoded'}
    driverOptions['phantomjs.page.settings.userAgent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
    #if taskData['proxy'] != 'localhost':
        #chromeOptions.add_extension(proxyPlugin)
    #chromeOptions.add_argument('disable-infobars')
    splashBrowser = webdriver.PhantomJS(desired_capabilities = driverOptions)
    splashBrowser.set_window_size(1920, 1080)
    splashBrowser.delete_all_cookies()
    return splashBrowser

def addGmailCookies(gmailCookies, splashBrowser):
    splashBrowser.get('https://www.google.com/')
    for cookie in gmailCookies:
        try:
            splashBrowser.add_cookie(cookie)
        except Exception as error:
            pass

def getSplash(config, taskData, splashBrowser):
    regions = {'au': 'https://www.adidas.com.au/',
               'uk': 'https://www.adidas.co.uk/',
               'fr': 'https://www.adidas.fr/',
               'ca': 'http://www.adidas.ca/',
               'us': 'http://www.adidas.com/us/'}
    for region in regions:
        if region == config['region']:
            regionHomepage = regions[region]
            taskData['region'] = region
    #print(time.strftime('[%I:%M:%S %p - Task ' + str(taskData['taskNumber']) + '] ') + 'Getting Region Homepage')
    #splashBrowser.get(regionHomepage)
    #print(time.strftime('[%I:%M:%S %p - Task ' + str(taskData['taskNumber']) + '] ') + 'Got Region Homepage')
    print(time.strftime('[%I:%M:%S %p - Task ' + str(taskData['taskNumber']) + '] ') + 'Getting Splash Page')
    splashBrowser.get(config['splashUrl'])
