# -*- coding: utf-8 -*-
__author__ = 'marco'

class Notifier:

    def SendMessage(self,message):
        self.__message = message
        import os
        os.system('terminal-notifier -message ' + '"' + self.__message + '"' +  ' -title ' + '"PySync "')

