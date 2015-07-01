# -*- coding: utf-8 -*-
__author__ = 'marco'

class GetFiles:

    def GetDir(self):
        return "dir.pysync"

    def GetUser(self):
        return "user.pysync"

    def GetServer(self):
        return "server.pysync"

    def GetMode(self):
        return "mode.pysync"

    def GetProto(self):
        return "proto.pysync"

    def GetMountpoint(self):
        return "mountpoint.pysync"



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
