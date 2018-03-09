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
    config['PID'] = configFile['PID']
    config['region'] = configFile['region']
    config['splashUrl'] = configFile['splashUrl']
    config['proxies'] = open(configFile['proxiesFile'] + '.txt', 'r').read().splitlines()
    config['webhookUrl'] = configFile['webhookUrl']
    return config


def initiateHeader(config):
    input('Press "Enter" To Initialize ' + str(len(config['proxies']))  + ' Tasks')

def gmailLogin():
    gmailBrowserOptions = Options()
    gmailBrowserOptions.add_argument('disable-infobars')
    gmailBrowserOptions.add_argument(':authority:accounts.google.com=accounts.google.com')
    gmailBrowserOptions.add_argument(':method:=GET')
    gmailBrowserOptions.add_argument(':path:=/ServiceLogin')
    gmailBrowserOptions.add_argument(':scheme:=https')
    gmailBrowserOptions.add_argument('Accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8')
    gmailBrowserOptions.add_argument('Accept-Encoding=gzip, deflate, br')
    gmailBrowserOptions.add_argument('Accept-Language=en-US,en;q=0.9')
    gmailBrowserOptions.add_argument('Upgrade-Insecure-Requests=1')
    gmailBrowserOptions.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
    gmailBrowser = webdriver.Chrome(chrome_options = gmailBrowserOptions)
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
