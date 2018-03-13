#!/bin/bash

echo Script de instalacion
sleep 2s

sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.6 -Y
sudo apt-get install python3-pip -Y
