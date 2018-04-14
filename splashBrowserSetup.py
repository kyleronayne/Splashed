import random
import zipfile
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
import time

def getUserAgent():
    userAgents = {'desktop': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0', 'mobile': ''}

def launchSplashBrowser(taskData, proxyPlugin):
    splashBrowserProfile = webdriver.FirefoxProfile()
    splashBrowserProfile.set_preference('general.useragent.override', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0')
    splashBrowserOptions = Options()
    splashBrowserOptions.add_argument('--headless')
    splashBrowser = webdriver.Firefox(splashBrowserProfile, firefox_options = splashBrowserOptions)
    splashBrowser.delete_all_cookies()
    splashBrowser.set_window_size(1550, 878)
    return splashBrowser

def addGmailCookies(gmailCookies, splashBrowser):
    splashBrowser.get('https://www.google.com/')
    for cookie in gmailCookies:
        splashBrowser.add_cookie(cookie)

def getSplash(config, taskData, splashBrowser):
    print(time.strftime('[%I:%M:%S %p - Task ' + str(taskData['taskNumber']) + '] ') + 'Getting Splash Page URL From Config')
    splashBrowser.get(config['splashUrl'])
