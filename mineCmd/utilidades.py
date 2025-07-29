from colorama import init, Fore, Style
import os, sys, time

init()

def simulacionCarga():
    for i in range(10):
        sys.stdout.write(f"\rCargando{'.' * (i % 4)}")
        sys.stdout.flush()
        time.sleep(0.4)

def barra_de_cargaVerde(duracion=5, largo=30):
    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "\n Iniciando proceso..." + Style.RESET_ALL)
    
    for i in range(largo + 1):
        porcentaje = int((i / largo) * 100)
        barras = '█' * i + '-' * (largo - i)
        sys.stdout.write(f"\r{Fore.GREEN}[{barras}] {porcentaje}%")
        sys.stdout.flush()
        time.sleep(duracion / largo)
def barra_de_cargaMorado(duracion=5, largo=30):
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "\n Iniciando proceso..." + Style.RESET_ALL)
    
    for i in range(largo + 1):
        porcentaje = int((i / largo) * 100)
        barras = '█' * i + '-' * (largo - i)
        sys.stdout.write(f"\r{Fore.MAGENTA}[{barras}] {porcentaje}%")
        sys.stdout.flush()
        time.sleep(duracion / largo)

    print(Fore.YELLOW + "\n Funcion cargada.\n" + Style.RESET_ALL)
def barra_de_cargaRojo(duracion=5, largo=30):
    print(Fore.LIGHTRED_EX+ Style.BRIGHT + "\n Iniciando proceso..." + Style.RESET_ALL)
    
    for i in range(largo + 1):
        porcentaje = int((i / largo) * 100)
        barras = '█' * i + '-' * (largo - i)
        sys.stdout.write(f"\r{Fore.GREEN}[{barras}] {porcentaje}%")
        sys.stdout.flush()
        time.sleep(duracion / largo)
def barra_de_cargaAzul(duracion=5, largo=30):
    print(Fore.LIGHTBLUE_EX+ Style.BRIGHT + "\n Iniciando proceso..." + Style.RESET_ALL)
    
    for i in range(largo + 1):
        porcentaje = int((i / largo) * 100)
        barras = '█' * i + '-' * (largo - i)
        sys.stdout.write(f"\r{Fore.BLUE}[{barras}] {porcentaje}%")
        sys.stdout.flush()
        time.sleep(duracion / largo)
def simulacionCargaRapida():
    for i in range(10):
        sys.stdout.write(f"\rCargando{'.' * (i % 4)}")
        sys.stdout.flush()
        time.sleep(0.1)