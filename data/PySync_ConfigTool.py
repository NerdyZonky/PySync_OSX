# -*- coding: utf-8 -*-
__author__ = 'marco'

import os
import getpass
import keyring
from files import *
from Output import *


#All information that PySync needs
get = GetFiles()
checkPath = CheckFiles()
checkData = CheckFiles()
directory = ReadFiles(get.GetDir())
user = ReadFiles(get.GetUser())
server = ReadFiles(get.GetServer())
mode = ReadFiles(get.GetMode())
proto = ReadFiles(get.GetProto())
mountpoint = ReadFiles(get.GetMountpoint())


#Check if config path exists
checkPath.checkPath()
#Check if config data exists
checkData.checkData()

#Getting menu
menu = Menu()

while True:

    menu.GetMainMenu()
    choose = raw_input()

    if choose == "0":
        print"Aktuelles Protokoll:"
        print"....................."
        proto.ReadFile()
        print".....................\n"
        print"Möchten Sie das aktuelle Protokoll wirlich ändern?"
        print"j/n"
        choose = raw_input()

        if choose == "n":
            print"Beende Programm"
            exit()

        if choose == "j":
            while True:
                menu.ProtoMenu()
                proto = raw_input()
                print"Neues Protokoll: %r \n" % proto
                print"Ist das neue Protokoll korrekt?"
                print"j/n/q"
                choose = raw_input()
                if choose == "j":
                    WriteProto = WriteFiles(get.GetProto(),proto)
                    WriteProto.WriteFile()
                    print"Modus wurde geändert!"
                    break
                if choose == "n":
                    continue

                if choose == "q":
                    break

    if choose == "1":
        print"Folgende Verzeichnisse sind aktuell gespeichert:"
        print"................................................"
        directory.ReadFile()
        print"................................................\n"
        print"Möchten Sie die Verzeichnisse wirklich ändern?"
        print"j/n"
        choose = raw_input()

        if choose == "n":
            pass

        if choose == "j":
            i = 0
            SRC = []
            DST = []

            while True:
                print "Bitte geben Sie das Quellverzeichnis",i+1, "ein:"
                SRC.append(raw_input())
                print "Bitte geben Sie das Zielverzeichnis", i+1, "ein:"
                DST.append(raw_input())

                print "Möchten Sie weitere Verzeichnisse angeben?"
                print "j/n"
                choose = raw_input()
                if choose == "j":
                     i=i+1

                if choose == "n":
                    print"Folgende Verzeichnisse wurden angegeben:"
                    print"................................................"
                    for i in range (len(SRC)):
                        print("Quelle: %r  Ziel: %r" %(SRC[i],DST[i]))
                    print"................................................\n"
                    print("Sind die Verzeichnisse korrekt?")
                    print"j/n/q"
                    choose = raw_input()
                    if choose == "n":
                        SRC = []
                        DST = []
                        continue
                    if choose == "j":
                        pass

                    if choose == "q":
                        break

                    fobj = open(get.GetDir(),"w")
                    print"Schreibe Änderungen...\n"
                    for i in range(len(SRC)):
                        fobj.write(str(SRC[i]) + ":" + DST[i])
                        fobj.write("\n")
                        fobj.close()

                    print"Verzeichnisse wurden Geändert!"
                    exit()

    if choose == "2":
        print"Was möchten Sie ändern?\n"
        print"1 = Username"
        print"2 = Servername"
        print"3 = Passwort (nicht nötig für SSH)"
        print"4 = Mountpoint (nicht nötig für SSH)"

        choose = raw_input()
        if choose == "1":
            print"Aktueller Username:"
            print"....................."
            user.ReadFile()
            print"....................."

            print"Möchten Sie Ihren Benutzernamen wirlich ändern?"
            print"j/n\n"
            choose = raw_input()
            if choose == "n":
               pass

            if choose =="j":
                while True:
                    print"Geben Sie den neuen Benutzernamen ein:"
                    user = raw_input()
                    print"Neuer Benutzername: %r \n" % user
                    print"Ist der neue Benutzername korrekt?"
                    print"j/n/q"
                    choose = raw_input()
                    if choose == "j":
                        WriteUser = WriteFiles(get.GetUser(),user)
                        WriteUser.WriteFile()
                        print"Benutzername wurde geändert!"
                        break
                    if choose == "n":
                        continue

                    if choose == "q":
                        break

        if choose == "2":

            print"Aktueller Servername:"
            print"....................."
            server.ReadFile()
            print".....................\n"

            print"Möchten Sie den Servernamen wirlich ändern?"
            print"j/n"
            choose = raw_input()
            if choose == "n":
                pass

            if choose =="j":
                while True:
                    print"Geben Sie den neuen Servernamen ein:"
                    server = raw_input()
                    print"Neuer Servername: %r \n" % server
                    print"Ist der neue Servername korrekt?"
                    print"j/n/q"
                    choose = raw_input()
                    if choose == "j":
                        WriteServer = WriteFiles(get.GetServer(),server)
                        WriteServer.WriteFile()
                        print"Servername wurde geändert!"
                        break
                    if choose == "n":
                        continue

                    if choose == "q":
                        break



        if choose == "3":
                print("Passwort:")
                p = getpass.getpass()
                print"Ist das neue Passwort korrekt?"
                print"j/n/q"
                choose = raw_input()
                if choose == "j":
                    keyring.set_password("PySync",user.ReadFile(),p)
                    print("PASSWORT:" + keyring.get_password("PySync",user.ReadFile()))
                    print"Passwort wurde geändert!"
                    print("PASSWORT:" + keyring.get_password("PySync",user.ReadFile()))
                    pass
                if choose == "n":
                    continue

                if choose == "q":
                   break

        if choose == "4":

            print"Aktueller Mountpoint:"
            print"....................."
            mountpoint.ReadFile()
            print".....................\n"

            print"Möchten Sie den aktuellen Mountpoint wirlich ändern?"
            print"j/n"
            choose = raw_input()
            if choose == "n":
                pass

            if choose =="j":
                while True:
                    print"Geben Sie den neuen Mountpoint ein:"
                    mountpoint = raw_input()
                    print"Neuer Mountpoint: %r \n" % mountpoint
                    print"Ist der neue Mountpoint korrekt?"
                    print"j/n/q"
                    choose = raw_input()
                    if choose == "j":
                        WriteMountpoint = WriteFiles(get.GetMountpoint(),mountpoint)
                        WriteMountpoint.WriteFile()
                        print"Servername wurde geändert!"
                        break
                    if choose == "n":
                        continue

                    if choose == "q":
                        break

    if choose == "3":
        print"Aktueller Modus:"
        print"....................."
        mode.ReadFile()
        print".....................\n"
        print"Möchten Sie den Modus wirlich ändern?"
        print"j/n"
        choose = raw_input()
        if choose == "n":
            print"Beende Programm"
            exit()

        if choose =="j":
            while True:
                print"Geben Sie den neuen Modus ein:"
                menu.ModeMenu()
                mode = raw_input()
                print"Neuer Modus: %r \n" % mode
                print"Ist der neue Modus korrekt?"
                print"j/n/q"
                choose = raw_input()
                if choose == "j":
                    WriteMode = WriteFiles(get.GetMode(),mode)
                    WriteMode.WriteFile()
                    print"Modus wurde geändert!"
                    break
                if choose == "n":
                    continue

                if choose == "q":
                    break

    if choose == "4":
        print"VERZEICHNISSE:"
        print"................................................"
        directory.ReadFile()
        print"................................................"
        print"BENUTZERNAME:"
        user.ReadFile()
        print"SERVERNAME:"
        server.ReadFile()
        print"MODUS:"
        mode.ReadFile()
        print "\n "
        print"zurück zum Menü = beliebige Taste"
        q = raw_input()
        if q == " ":
            pass


    if choose == "5":
        swap = ReadFilesRsync(get.GetMode())
        swap2 = swap.ReadFile()
        fobj = open(get.GetMode(),"w")
        fobj.write("--try " + swap2 )
        fobj.close()
        os.system("python main.py")
        fobj = open(get.GetMode(),"w")
        fobj.write(swap2)
        fobj.close()
        print"Synchronisationstest abgeschlossen. Zurück zum Menü?"
        print"j/n"
        z = raw_input()
        if z == "j":
            pass

        if z == "n":
            print"Beende PySync"
            print"Ciao!"
            exit()


    if choose == "6":
        os.system("python main.py")
        print"Manuelle Synchronisation abgeschlossen. Zurück zum Menü?"
        print"j/n"
        z = raw_input()
        if z == "j":
            pass

        if z == "n":
            print"Beende PySync"
            print"Ciao!"
            exit()


    if choose == "7":
        swap = ReadFilesRsync(get.GetMode())
        swap2 = swap.ReadFile()
        fobj = open(get.GetMode(),"w")
        fobj.write("-p")
        fobj.close()
        os.system("python main.py")
        fobj = open(get.GetMode(),"w")
        fobj.write(swap2)
        fobj.close()
        print"Daten wurden zurück gespielt. Zurück zum Menü?"
        print"j/n"
        z = raw_input()
        if z == "j":
            pass

        if z == "n":
            print"Beende PySync"
            print"Ciao!"
            exit()

    if choose == "8":
        print"Beende PySync"
        print"Ciao!"
        exit()