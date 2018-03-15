import requests
import time

def notify(taskData, config):
    if config['webhookUrl'] != None:
        notification = {'username': 'A1 Adidas Notifications',
                        'text': '*PASSED SPLASH - ' + config['region'].upper() + '*',
                        'attachments': {'fields': [{'title': 'Task',
                                                    'value': taskData['taskNumber']},
                                                   {'title': 'PID',
                                                    'value': config['PID']},
        			                               {'title': 'Proxy',
        			                                'value': taskData['proxy']},
                                                   {'title': 'Sitekey',
                                                    'value': taskData['sitekey']}],
                        'color': '#39FF14'}}
        try:
            requests.post(config['webhookUrl'], json = notification)
        except:
            print(time.strftime('[%I:%M:%S %p - Task ' + str(taskData['taskNumber']) + '] ') + 'Error Sending Slack Notification, Check Webhook Url')
