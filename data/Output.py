# -*- coding: utf-8 -*-
__author__ = 'marco'

class Menu:

    def GetMainMenu(self):
        import os
        os.system("clear")
        print "PySync ConfigTool Ver. 0.9.6"
        print "Copyright (C) 2015  NerdyZonky"
        print "Was möchten Sie tun?\n"

        print "......................................."
        print "0 = Setze Protokoll"
        print "1 = Setze Verzeichnisse"
        print "2 = Setze Benutzer- und Servernamen"
        print "3 = Setze Modus"
        print "4 = Überprüfe Konfiguration"
        print "5 = Teste Synchronisation"
        print "6 = Manuelle Synchronisation"
        print "7 = Spiele Daten zurück"
        print "8 = Beende Programm"
        print ".......................................\n"


    def ModeMenu(self):
        print'''
Sie haben folgende Möglichkeiten:

-d = Default Sync: Es werden keine Daten im Zielordner gelöscht
-i = Inkrementeller Sync: Daten die im Quellordner gelöscht werden, werden auch im Zielordner gelöscht
-s = Safe Sync: Daten die im Quellordner gelöscht werden, werden in einen gesonderten Ordner übertragen
'''
    def ProtoMenu(self):
        print'''
Sie haben folgende Möglichkeiten:

ssh = Secure Shell(Unix)
smb = Windows Share
afp = Apple Share
nfs = Unix Share (noch nicht implementiert)
'''
