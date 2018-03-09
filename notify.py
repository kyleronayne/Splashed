import requests
import time

def notify(taskData, config):
    notification = {'username': 'A1 Adidas Notifications',
                    'text': '*PASSED SPLASH - ' + config['region'].upper() + '*',
                    'attachments': {'fields': [{'title': 'Task',
                                                'value': taskData['taskNumber'],
                                                'short': True},
                                               {'title': 'PID',
                                                'value': config['PID'],
                                                'short': True},
    			                               {'title': 'Proxy',
    			                                'value': taskData['proxy'],
                                                'short': True},
                                               {'title': 'Sitekey',
                                                'value': taskData['sitekey'],
                                                'short': True}],
                    'color': '#39FF14'}}
    resp = requests.post(config['webhookUrl'], json = notification)
    if resp.status_code == 404:
        print(time.strftime('[%I:%M:%S %p - Task ' + str(taskData['taskNumber']) + '] ') + 'Error Sending Slack Notification, Check Webhook Url')
