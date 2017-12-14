import random
from selenium.webdriver.chrome.options import Options
import zipfile
from seleniumrequests import Chrome
from selenium.common.exceptions import TimeoutException
import time


def launchSplashBrowser(taskData, proxyPlugin):
    chromeOptions = Options()
    chromeOptions.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
    if taskData['proxy'] != 'localhost':
        chromeOptions.add_extension(proxyPlugin)
    chromeOptions.add_argument('disable-infobars')
    splashBrowser = Chrome(chrome_options = chromeOptions)
    splashBrowser.set_window_position(1000, 1000)
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
    print(time.strftime('[%I:%M:%S %p - Task ' + str(taskData['taskNumber']) + '] ') + 'Getting Region Homepage')
    splashBrowser.get(regionHomepage)
    print(time.strftime('[%I:%M:%S %p - Task ' + str(taskData['taskNumber']) + '] ') + 'Got Region Homepage')
    print(time.strftime('[%I:%M:%S %p - Task ' + str(taskData['taskNumber']) + '] ') + 'Getting Splash Page')
    splashBrowser.get(config['splashUrl'])
    print(time.strftime('[%I:%M:%S %p - Task ' + str(taskData['taskNumber']) + '] ') + 'Waiting On Splash Page')
