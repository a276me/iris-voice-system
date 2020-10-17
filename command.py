import re
import apps


class Command:

    def __init__(self, cmd):
        self.cmd = cmd
        self.app = 'unknown'
        self.object = None

        # get rid of unnecessary words
        self.cmd = re.sub(r' is| a| the|can you |please | please|may you ','',self.cmd)

        for app in apps.routes:
            if re.search('|'.join(app['keys']), self.cmd):
                self.app = app['name']
                self.object = app

        # # define the magitude and action of the command
        # if re.search(r'down|decrease',self.cmd):
        #     self.action = 'N'
        # elif re.search(r'close|off|of|shut', self.cmd):
        #     self.action = 'N'
        #     self.magnitude = 'high'
        # elif re.search(r'up|raise|increase',self.cmd):
        #     self.action = 'P'
        # elif re.search(r'turn on|open|on', self.cmd):
        #     self.action = 'P'
        #     self.magnitude = 'high'
        #
        # # define what object does the command want to do
        # if re.search(r'TV|television|tv', self.cmd):
        #     self.object = 'TV'
        # elif re.search(r'lights|brightness|light', self.cmd):
        #     self.object = 'light'
        # elif re.search(r'volume|sound', self.cmd):
        #     self.object = 'volume'


    def __str__(self):
        return str({'cmd': self.cmd, 'app': self.app, 'obj': self.object})


