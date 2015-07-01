# -*- coding: utf-8 -*-
__author__ = 'marco'


from osx_notifier import Notifier
from files import GetFiles
from files import ReadFilesRsync
from ping import ping
from ssh_sync import ssh
from volume_sync import volume


get = GetFiles()
Send = Notifier()
user = ReadFilesRsync(get.GetUser())
server =(ReadFilesRsync(get.GetServer()))
mode = ReadFilesRsync(get.GetMode())


#Checking if server is online
serverping = server.ReadFile()
ping = ping(serverping)
ping.pingServer()



#Checking which protocol is used
proto = ReadFilesRsync(get.GetProto())

if proto.ReadFile() == "ssh":
    sync = ssh()
    sync.sshSync()

else:

    sync = volume()
    sync.volumeSync()