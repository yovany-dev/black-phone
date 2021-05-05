#!/bin/bash

#Colours
greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
purpleColour="\e[0;35m\033[1m"
turquoiseColour="\e[0;36m\033[1m"
grayColour="\e[0;37m\033[1m"


pkg update > /dev/null 2>&1
pkg upgrade -y > /dev/null 2>&1
pkg install -y git > /dev/null 2>&1

git clone https://github.com/Yovany-Black-Hat/Black-Phone.git > /dev/null 2>&1
mv Black-Phone/* .
rm -rf Black-Phone
chmod 777 install.sh

echo -e "\n\n    ${greenColour}[${redColour}*${greenColour}] Script actualizado y configurado${endColour}"
echo -e "    ${greenColour}[${redColour}!${greenColour}] El Script se reiniciara automaticamente...${endColour}"
sleep 5s

python3 main.py
