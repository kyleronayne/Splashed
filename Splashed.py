from setup import setup, setTaskData, startTasks
from proxyHandling import proxyHandling
import threading
from splashBrowserSetup import launchSplashBrowser, addGmailCookies, getSplash
from productDetection import productDetection
from showChecokutBrowser import showCheckoutBrowser
import time

config, gmailCookies = setup()

def main(gmailCookies, taskData, proxyPlugin):
    splashBrowser = launchSplashBrowser(taskData, proxyPlugin)
    addGmailCookies(gmailCookies, splashBrowser)
    getSplash(config, taskData, splashBrowser)
    productDetection(splashBrowser, taskData)
    showCheckoutBrowser(splashBrowser, taskData, config)

def createTasks(config, gmailCookies):
    tasks = []
    taskNumber = 0
    for i in range(0, len(config['proxies'])):
        taskNumber += 1
        taskData = setTaskData()
        taskData['taskNumber'] = taskNumber
        proxyPlugin = proxyHandling(config, taskData)
        task = threading.Thread(target = main, args = (gmailCookies, taskData, proxyPlugin,))
        tasks.append(task)
    startTasks(config)
    for task in tasks:
        time.sleep(.5)
        task.start()
createTasks(config, gmailCookies)
