# -*- coding: utf-8 -*-
__author__ = 'marco'

class Menu:

    def GetLicence(self):
        print '''
PySync ConfigTool Ver. 0.9
Copyright (C) 2015  Marco Schubert

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program; if not, see http://www.gnu.org/licenses/.
'''

    def GetMainMenu(self):

        print "\n"
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

smb = Windows Share
afp = Apple Share
nfs = Unix Share (noch nicht implementiert)
'''