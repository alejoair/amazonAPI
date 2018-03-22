#!/bin/bash
echo Script de instalacion
sleep 2s
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.6 -y
sudo apt-get install python3-pip -y
sudo apt-get install git -y
sudo apt-get install supervisor -y
echo Instalando Django y Paquetes
sleep 2s
sudo apt-get install libxml2-dev libxslt-dev python-dev -y
sudo apt-get install python3-lxml -y
sudo apt-get build-dep python3-lxml -y
pip3 install lxml
pip3 install bs4
pip3 install requests
pip3 install django
pip3 install gunicorn
pip3 install mysqlclient
pip3 install django-summernote
echo Descargando Repositorio GIT
git clone https://github.com/alejoair/MerchM.git
cd MerchM
echo Iniciar Servidor
gunicorn merchSearch.wsgi --bind 0.0.0.0:80

git install supervisor -y

[program:scriptstart]
command = /root/s.bash
user = root
stdout_logfile = /root/log.log
redirect_stderr = true
environment=LANG=en_US.UTF-8,LC_ALL=en_US.UTF-8

#!/bin/bash
cd /root/amazonAPI/api
python3 manage.py runserver 0.0.0.0:80