# -*- coding: utf-8 -*-
__author__ = 'marco'

class volume:

    def volumeSync(self):

        import os
        import keyring
        from rsyncVolume import rsync
        from files import GetFiles
        from files import ReadFilesRsync
        from mount import mount

        get = GetFiles()


        #Setting variables
        user = ReadFilesRsync(get.GetUser())
        server = (ReadFilesRsync(get.GetServer()))
        mode = ReadFilesRsync(get.GetMode())
        mountpoint = ReadFilesRsync(get.GetMountpoint())
        proto = ReadFilesRsync(get.GetProto())


        #Setting constructor
        x = keyring.get_password("PySync","Py")
        y = proto.ReadFile()
        z = server.ReadFile()
        u = user.ReadFile()
        m = mountpoint.ReadFile()


        #Start mount class
        mount = mount(y,z,u,x,m)
        mount.mountVolume()


        #Get directories
        print"Hole Verzeichnisse"
        directory = []
        i = 0
        fobj = open(get.GetDir())
        for line in fobj:
            directory.append(line.rstrip())
            i = i+1
        fobj.close()

        SRC = []
        DST = []

        check = mode.ReadFile()

        if check == "-p":
            for i in range (len(directory)):
                tmp = directory[i].split(":")
                tmp1 = tmp[0]
                tmp2 = tmp1.split("/")
                tmp3 = "/%s" % tmp2[-1]
                tmp4 = tmp[1]
                tmp2.pop()
                tmpSRC = ("/").join(tmp2)
                tmpDST = tmp[1] + tmp3
                DST.append(tmpDST)
                SRC.append(tmpSRC)

        else:
            for i in range (len(directory)):
                tmp = directory[i].split(":")
                SRC.append(tmp[0])
                DST.append(tmp[1])


        #Starting Sync
        print "Starte Sync..."
        for i in range (len(SRC)):
            print "DST: %s SRC: %s" % (SRC[i], DST[i])
            sync = rsync(SRC[i], DST[i], mode.ReadFile())
            sync.Sync()

        volume = "/Volumes/" + m
        os.system("umount " + volume)
        exit()