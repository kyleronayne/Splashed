from setup import setup, setTaskData, startTasks
from proxyHandling import proxyHandling
import threading
from splashBrowserSetup import launchSplashBrowser, addGmailCookies, getSplash
from productDetection import productDetection
from showSplashBrowser import showSplashBrowser

config, gmailCookies = setup()

def main(taskData, gmailCookies, splashBrowser):
    addGmailCookies(gmailCookies, splashBrowser)
    getSplash(config, taskData, splashBrowser)
    productDetection(splashBrowser, taskData)
    showSplashBrowser(splashBrowser, taskData)

def createTasks(config, gmailCookies):
    tasks = []
    taskNumber = 0
    for i in range(0, len(config['proxies'])):
        taskNumber += 1
        taskData = setTaskData()
        taskData['taskNumber'] = taskNumber
        proxyPlugin = proxyHandling(config, taskData)
        splashBrowser = launchSplashBrowser(taskData, proxyPlugin)
        task = threading.Thread(target = main, args = (taskData, gmailCookies, splashBrowser))
        tasks.append(task)
    startTasks(config)
    for task in tasks:
        task.start()
createTasks(config, gmailCookies)
