#!/bin/bash

greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
symbol="${greenColour}[${redColour}*${greenColour}]"
symbolTwo="${greenColour}[${redColour}!${greenColour}]${endColour}"
chmod 777 update.sh


clear
echo -e "${symbol} Actualizando paquetes...\n${endColour}"
pkg update -y
pkg upgrade -y


clear
echo -e "${symbol} Instalando Python3\n${endColour}"
pkg install python -y


clear
echo -e "${symbol} Instalando modulos de Python3...\n${endColour}"
pip install requests


clear
echo -e "${symbol}${blueColour} Paquetes instalados correctamente.${endColour}"
echo -e "\n${symbolTwo}${redColour} Ejecute: ${greenColour}python3 main.py${endColour}"
