'''
#########################################################
## ====================================================##
## DOCUMENTACIÓN:                                      ##
## Creación: 30 / 3 / 2021                             ##
## Ultima Actualización: 4 / 7 / 2021                  ##
# Versión: v1.5.0                                      ##
## ====================================================##
## Programa escrito y dessarrollado por Edu Olivares   ##
## Sistema de Register / Login Inovador :D             ##
## Espero que en un futuro esto sirva de algo...       ##
## ====================================================##
#########################################################
'''



import random
from colorama import Fore, Style, init
import base64
import time

# Declaramos todas las veriables
fecha = time.strftime("%d-%m-%y %X")
fecha2 = time.strftime("%x")
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
nums = "9183726450"
init(autoreset=True)

username = input(Fore.GREEN + '[+] ' + Style.RESET_ALL + 'Introduce un nombre de usuario: ')

for c in range(1):

    part1 = ""
    part2 = ""
    part3 = fecha2

    for x in range(10):
        part1 += random.choice(nums) # Selecionamos 10 números aleatorios como si fuera la ID
    for x in range(7):
        part2 += random.choice(chars) # 7 números aleatorios

    part1 = str(part1)
    part2 = str(part2)
    part3 = str(part3)

############################## CODIFICACIÓN ##############################
    # Codificamos la ID en Base64
    encodedBytes = base64.b64encode(part1.encode("utf-8"))
    part1encode = str(encodedBytes, "utf-8")

    # Codificamos la Fecha en Base64
    encodedBytes = base64.b64encode(part3.encode("utf-8"))
    part3encode = str(encodedBytes, "utf-8")

##########################################################################

    # Juntamos todas las partes
    gato = part1encode + "." + part2 + "." + part3encode

    # Mostramos el Gato creado
    print(Fore.BLUE + '[?] ' + Style.RESET_ALL + 'El Gato para ' + Style.BRIGHT + username + ' es: ' + Fore.YELLOW + gato)
    print(Fore.BLUE + '[?] ' + Style.RESET_ALL + 'La ID del usuario ' + Style.BRIGHT + username + ' es: ' + Fore.YELLOW + part1)
    print(Fore.BLUE + '[?] ' + Style.RESET_ALL + 'La Fecha de creación del Gato es el: ' + Fore.YELLOW + fecha)

# Estas dos lineas es para adaptar el programa a un ejecutable .exe
exit = input('Pulse enter para salir...')
exit = quit()