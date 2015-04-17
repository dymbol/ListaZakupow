#!/bin/bash
#change to desired bind ip address 
ip=192.168.56.101
port=8000

python manage.py runserver $ip:$port
