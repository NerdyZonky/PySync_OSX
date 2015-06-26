# -*- coding: utf-8 -*-
__author__ = 'marco'


class rsync:

    def __init__(self,source,target,user,server,modus):
        self.__source = source
        self.__target = target
        self.__user = user
        self.__server = server
        self.__modus = modus

    def ssh(self):

        import os


        if self.__modus == '-d':
            print('Default SSH-Sync wird gestartet')
            os.system('rsync -avz --iconv=utf-8-mac,utf-8 --exclude=exdir.txt ' + self.__source + ' -e ssh '+ self.__user+'@'+self.__server+':'+self.__target)

        elif self.__modus == '-i':
            print('Inkrementeller SSH-Sync wird gestartet')
            os.system('rsync --delete -avz --iconv=utf-8-mac,utf-8 --exclude=exdir.txt ' + self.__source + ' -e ssh '+ self.__user+'@'+self.__server+':'+self.__target)

        elif self.__modus == '-s':
            print('Safe SSH-Sync wird gestartet')
            os.system('rsync --exclude=exdir.txt --iconv=utf-8-mac,utf-8 --backup-dir='+self.__target+'/deleted' + ' --delete -avzb ' + self.__source + ' -e ssh '+ self.__user+'@'+self.__server+':'+self.__target)

        elif self.__modus == '-p':
            print('Playback über SSH wird gestartet')
            os.system('rsync --progress --iconv=utf-8,utf-8-mac -avzbe ssh '+self.__user+'@'+self.__server+':'+ self.__target + " " + self.__source)


        elif self.__modus == '--try -d':
            print('Teste Default SSH-Sync')
            os.system('rsync -navz --iconv=utf-8-mac,utf-8 --exclude=exdir.txt ' + self.__source + ' -e ssh '+ self.__user+'@'+self.__server+':'+self.__target)

        elif self.__modus == '--try -i':
            print('Teste Inkrementellen SSH-Sync')
            os.system('rsync --delete -navz --iconv=utf-8-mac,utf-8 --exclude=exdir.txt ' + self.__source + ' -e ssh '+ self.__user+'@'+self.__server+':'+self.__target)

        elif self.__modus == '--try -s':
            print('Teste Safe SSH-Sync')
            os.system('rsync --exclude=exdir.txt --iconv=utf-8-mac,utf-8 --backup-dir='+self.__target+'/deleted' + ' --delete -navzb ' + self.__source + ' -e ssh '+ self.__user+'@'+self.__server+':'+self.__target)


        elif self.__modus == '--try -p':
            print('Teste Playback SSH-Sync')
            os.system('rsync --progress --iconv=utf-8,utf-8-mac -navzbe ssh '+self.__user+'@'+self.__server+':'+ self.__target + " " + self.__source)
        else:
            print ('Falscher Parameter in mode')
            print('Default SSH-Sync wird gestartet')
            exit()