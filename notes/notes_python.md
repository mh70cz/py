python:
default 3:
from root account:

https://stackoverflow.com/questions/41986507/unable-to-set-default-python-version-to-python3-in-ubuntu

update-alternatives --install /usr/bin/python python /usr/bin/python3 100

problém je, že se jedná o 3.5 (který musí v systému zůstat)
řešení nainstalovat 3.6 a vscode změnit "python.pythonPath": "python3.6"

install 3.6:
***

sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt-get update
sudo apt-get install python3.6  (nainstaluje 3.6.1)


root@DellT3400:/home/mh70# python --version (po update-alternatives)
Python 3.5.2
root@DellT3400:/home/mh70# python2 --version
Python 2.7.12
root@DellT3400:/home/mh70# python3 --version
Python 3.5.2
root@DellT3400:/home/mh70# python3.6 --version
Python 3.6.1+

***
pylint nainstalovat pro konkrétní verzi (3.6)
python3.6 -m pip install pylint

***
