# -*- coding: utf-8 -*-
from ircbotframework.bot import MODE_OPERATOR
from ircbotframework.plugin import BasePlugin, RegistryDictionary
from twisted.internet import reactor
import os
import subprocess


PROJECT_DIR = os.path.join(os.path.dirname(__file__), '..')

def get_revision():
    gitdir = os.path.join(PROJECT_DIR, '.git')
    headfile = os.path.join(gitdir, 'HEAD')
    with open(headfile) as fobj:
        head = fobj.read().strip()
    if head.startswith('ref: '):
        headref = head[5:]
        reffile = os.path.join(gitdir, headref)
        with open(reffile) as fobj:
            head = fobj.read().strip()
    return head

class Update(BasePlugin):
    commands = RegistryDictionary()
    
    def handle_joined(self, channel):
        channel.msg("%s running at %s" % (self.protocol.nickname, get_revision()))
    
    @commands('update')
    def update(self, rest, channel, user):
        if user.mode >= MODE_OPERATOR:
            channel.msg('Updating (all commands disabled)...')
            self.protocol.plugins = []
            subprocess.check_call(['git', 'pull', 'origin', 'master'], cwd=PROJECT_DIR)
            subprocess.check_call(['env/bin/pip', 'install', '-r', 'requirements.txt'], cwd=PROJECT_DIR)
            reactor.stop()
