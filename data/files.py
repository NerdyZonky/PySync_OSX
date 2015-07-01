# -*- coding: utf-8 -*-
__author__ = 'marco'

import os

path = os.environ['HOME'] + "/PySync/"


class GetFiles:


    def GetDir(self):
        dirpath = path + "dir.pysync"
        return dirpath

    def GetUser(self):
        userpath = path + "user.pysync"
        return userpath

    def GetServer(self):
        serverpath = path + "server.pysync"
        return serverpath

    def GetMode(self):
        modepath = path + "mode.pysync"
        return modepath

    def GetProto(self):
        protopath = path + "proto.pysync"
        return protopath

    def GetMountpoint(self):
        mountpointpath = path + "mountpoint.pysync"
        return mountpointpath

class CheckFiles(GetFiles):

    def checkPath(self):
        if os.path.exists(path) == False:
            os.system("mkdir %s" % path)

    def checkData(self):

        data = GetFiles()
        if os.path.exists(data.GetDir() ) == False:
            os.system("touch " + data.GetDir())

        if os.path.exists(data.GetUser() ) == False:
            os.system("touch " + data.GetUser())

        if os.path.exists(data.GetServer())== False:
            os.system("touch " + data.GetServer())

        if os.path.exists(data.GetMode())== False:
            os.system("touch " + data.GetMode())

        if os.path.exists(data.GetProto())== False:
            os.system("touch " + data.GetProto())

        if os.path.exists(data.GetMountpoint())== False:
            os.system("touch " + data.GetMountpoint())


class ReadFiles:

    def __init__(self,file):
        self._file = file


    def ReadFile(self):
        fobj = open(self._file)
        for line in fobj:
            print line.rstrip()
        fobj.close()

class ReadFilesRsync:

    def __init__(self,file):
        self._file = file


    def ReadFile(self):
        fobj = open(self._file)
        for line in fobj:
            return line.rstrip()
        fobj.close()


class WriteFiles(ReadFiles):

    def __init__(self,file,parameter):
        ReadFiles.__init__(self,file)
        self.__parameter = parameter

    def WriteFile(self):
        fobj = open(self._file,"w")
        print"Schreibe Änderungen...\n"
        fobj.write(self.__parameter)
        fobj.close()
