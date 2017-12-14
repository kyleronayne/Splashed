import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

def welcomeHeader():
    print('-- Splah Bot Developed By A1pickups --')
    print('Version: Beta')
    print()

def getConfig():
    config = {}
    configFile = eval(open('config.txt', 'r').read())
    config['region'] = configFile['region']
    config['splashUrl'] = configFile['splashUrl']
    config['proxies'] = open(configFile['proxiesFile'] + '.txt', 'r').read().splitlines()
    return config


def initiateHeader(config):
    input('Press "Enter" To Initialize ' + str(len(config['proxies']))  + ' Tasks')

def gmailLogin():
    chromeOptions = Options()
    chromeOptions.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
    chromeOptions.add_argument('disable-infobars')
    gmailBrowser = webdriver.Chrome(chrome_options = chromeOptions)
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
    print(time.strftime('[%I:%M:%S %p - General] ') + 'Starting All Tasks!')


def setTaskData():
    taskData = {'taskNumber': ''
                'region': '',
                'proxy': ''}
    return taskData

def setup():
    welcomeHeader()
    config = getConfig()
    initiateHeader(config)
    gmailCookies = gmailLogin()
    return config, gmailCookies
