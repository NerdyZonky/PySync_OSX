# -*- coding: utf-8 -*-
__author__ = 'marco'


class rsync:

    def __init__(self, source, target, modus):
        self.__source = source
        self.__target = target
        self.__modus = modus

    def Sync(self):

        import os
        from files import GetFiles
        from files import ReadFilesRsync
        get = GetFiles()
        mountpoint = ReadFilesRsync(get.GetMountpoint())

        if self.__modus == '-d':
            print('Default Sync wird gestartet')
            os.system('rsync -av --progress ' +    self.__source + " " + self.__target + ' --exclude=exdir.txt')

        elif self.__modus == '-i':
            print('Inkrementeller Sync wird gestartet')
            os.system('rsync -av --progress --delete ' + self.__source + " " + self.__target+ ' --exclude=exdir.txt')

        elif self.__modus == '-s':
            print('Safe Sync wird gestartet')
            os.system('rsync -avb --progress --delete ' + self.__source + " " + self.__target+ ' --exclude=exdir.txt --backup-dir='+self.__target+'/deleted')

        elif self.__modus == '-p':
            print('Playback-Sync wird gestartet')
            os.system('rsync -av --progress '+ self.__target + " " + self.__source)

        elif self.__modus == '--try -d':
            print('Teste Default Sync')
            os.system('rsync -nav --progress ' + self.__source + " " + self.__target+ ' --exclude=exdir.txt')

        elif self.__modus == '--try -i':
            print('Teste Inkrementellen Sync')
            os.system('rsync -nav --progress --delete ' + self.__source + " " + self.__target+ ' --exclude=exdir.txt')

        elif self.__modus == '--try -s':
            print('Teste Safe SSH-Sync')
            os.system('rsync -avb --progress --delete ' + self.__source + " " + self.__target+ ' --exclude=exdir.txt --backup-dir='+self.__target+'/deleted')

        elif self.__modus == '--try -p':
            print('Teste Playback SSH-Sync')
            os.system('rsync  -nav --progress '+ self.__target + " " + self.__source)

        else:
            print ('Falscher Parameter in mode')
            exit()