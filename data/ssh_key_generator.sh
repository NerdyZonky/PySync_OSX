#!/bin/bash

echo -e "PySync SSH Generator Ver. 0.2\n"
echo -e "Möchten Sie wirklich einen neuen SSH-Schlüssel generieren?\n"
echo -e "j/n\n"

read choose

if [ $choose = "n" ];then
	echo -e "Beende Programm\n"
	exit 0
fi

if [ $choose = "j" ];then
	
	echo -e "Generiere SSH-Key...\n"
	ssh-keygen -b 4096
	echo -e "Generierung abgeschlossen!\n"
	echo -e "Bereite Übertragung auf Remote Server vor..."
	echo -e "Geben Sie den Netzwerknamen des Servers ein!\n"
	read server
	echo $server >> /Applications/PySync_OSX/data/server.pysync
	echo -e "Geben Sie den Benutzernamen für $server ein"
	read user
	echo "Public Key wird auf Remoteserver übertragen..."
	scp ~/.ssh/id_rsa.pub $user@$server:~
	echo -e "Public Key Übertragung abgeschlossen!\n"
	echo -e "Verbinde zu $server..."
	ssh $user@$server 'bash -s' < /Applications/Pysync_OSX/data/TransferKey.sh
	echo -e " Keys wurden erfolgreich übertragen!\n"
	

		 
	echo -e "SSH-Schlüssel-Generierung abgeschlossen!"
	exit 0
fi