# -*- coding: utf-8 -*-
__author__ = 'marco'

import keyring

class mount:


    def __init__(self,proto, server,user,password,mountpoint):
        self.__proto = proto
        self.__server = server
        self.__user = user
        self.__password = password
        self.__mountpoint = mountpoint


    def mountVolume (self):

        import os
        from osx_notifier import Notifier
        from files import GetFiles
        from files import ReadFilesRsync

        message = Notifier()
        get = GetFiles()
        mountpoint = ReadFilesRsync(get.GetMountpoint())
        m = mountpoint.ReadFile()
        volume = "/Volumes/" + m


        #Checking which protocol
        if self.__proto == "smb":
            self.__proto = "smbfs //"

        if self.__proto == "afp":
            self.__proto = "afp afp://"


        #Create dir to mount drive
        print("Binde Netzlaufwerk ein...")
        message.SendMessage("Binde Netzlaufwerk ein...")
        os.system("umount " + volume)
        os.system("rm -r " + volume)
        os.system("mkdir " + volume)


        #Mount drive
        os.system("mount -t " + self.__proto + self.__user + ":" + self.__password + "@" + self.__server +"/"+self.__mountpoint + " " + volume)
        print("Netzlaufwerk erfolgreich eingebunden!")
        message.SendMessage("Netzlaufwerk erfolgreich eingebunden!")