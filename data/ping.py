__author__ = 'marco'

class ping:

    def __init__(self,ipServer):
        self.__ipserver = ipServer


    def pingServer(self):
        import os
        from osx_notifier import Notifier
        message = Notifier()

        message.SendMessage("Suche %s" % self.__ipserver)
        ping = os.system("ping -c 1 " + self.__ipserver)


        if ping == 0:
            print "%s erreichbar" %self.__ipserver
            message.SendMessage("%s ist erreichbar." % self.__ipserver)

        else:
            print  "%s ist nicht erreichbar! Beende Programm!" %self.__ipserver
            message.SendMessage("%s ist nicht erreichbar. Beende Programm!" % self.__ipserver)
            exit()
