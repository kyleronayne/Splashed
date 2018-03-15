import time
from selenium.webdriver.firefox.options import Options
from selenium import webdriver

def welcomeHeader():
    print('-- Splah Bot Developed By A1pickups --')
    print('Version: Beta')
    print()

def getConfig():
    config = {}
    configFile = eval(open('config.txt', 'r').read())
    config['PID'] = configFile['PID']
    config['region'] = configFile['region']
    config['splashUrl'] = configFile['splashUrl']
    config['proxies'] = open(configFile['proxiesFile'] + '.txt', 'r').read().splitlines()
    config['webhookUrl'] = configFile['webhookUrl']
    return config


def initiateHeader(config):
    input('Press "Enter" To Initialize ' + str(len(config['proxies']))  + ' Tasks')

def gmailLogin():
    gmailBrowserProfile = webdriver.FirefoxProfile()
    gmailBrowserProfile.set_preference('general.useragent.override', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0')
    gmailBrowserOptions = Options()
    gmailBrowserOptions.add_argument('--disable-extensions')
    gmailBrowserOptions.add_argument('--disable-infobars')
    gmailBrowser = webdriver.Firefox(gmailBrowserProfile, firefox_options = gmailBrowserOptions)
    gmailBrowser.delete_all_cookies()
    gmailBrowser.set_window_position(600, 0)
    gmailBrowser.get('https://accounts.google.com/ServiceLogin')
    print()
    input('Press "Enter" Once Logged In To Gmail')
    gmailCookies = gmailBrowser.get_cookies()
    gmailBrowser.quit()
    return gmailCookies

def startTasks(config):
    print()
    print('All Tasks Successfully Initialized!')
    print()
    input('Press "Enter" To Start Tasks')
    print()
    print('-- Log --')
    print(time.strftime('[%I:%M:%S %p] ') + 'Starting All Tasks!')


def setTaskData(config):
    taskData = {'region': '',
                'taskNumber': '',
                'proxy': '',
                'sitekey' : ''}
    return taskData

def setup():
    welcomeHeader()
    config = getConfig()
    initiateHeader(config)
    gmailCookies = gmailLogin()
    return config, gmailCookies
