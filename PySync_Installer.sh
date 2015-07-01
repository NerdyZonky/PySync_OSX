#!/bin/bash

echo "PySync wird installiert..."
echo "Löse Abhängigkeiten auf..."
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew -v update
brew install caskroom/cask/brew-cask
brew-cask install python
easy_install keyring
brew install terminal-notifier
brew install git


