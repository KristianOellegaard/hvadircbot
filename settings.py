# -*- coding: utf-8 -*-

NETWORK = 'irc.freenode.net'
PORT = 6667
CHANNEL = '#django-hvad'
NICKNAME = 'VikingBot'
PLUGINS = [
    'plugins.faq.FAQ',
    'plugins.issues.Issues',
    'plugins.update.Update',
]

GITHUB_USER = 'KristianOellegaard'
GITHUB_PROJECT = 'django-hvad'
WEBHOOKS = True
WEBHOOK_PORT = 9876

