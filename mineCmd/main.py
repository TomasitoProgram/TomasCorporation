import  keyboard, os, time, sys
from colorama import init, Fore, Style
from utilidades import simulacionCarga  
from autoClicker import autoclicker
from mobKiller import mobKiller
from farmBot import farmBot
from autoMiner import autoMiner


init()
os.system('cls')


print(Fore.GREEN + Style.BRIGHT + "Iniciando Script...")
simulacionCarga()
os.system('cls')
time.sleep(2)
print("TomásCorporation")  # DEAAAAH
time.sleep(1)
os.system('cls')
time.sleep(1)
print("\n¡Listo!")
time.sleep(1)
def mostrar_menu():
    os.system('cls')
    print(Fore.MAGENTA + Style.BRIGHT + "╔═══════════════════════════════════════════════╗")
    print("║            Minecraft Tools Launcher           ║")
    print("╚═══════════════════════════════════════════════╝" + Style.RESET_ALL)
    print(Fore.CYAN + Style.BRIGHT + "\nElige una herramienta:")
    print(Fore.MAGENTA + "[1] AutoClicker")
    print(Fore.MAGENTA + "[2] Farm Bot Simple")
    print(Fore.MAGENTA + "[3] MobKiller")
    print(Fore.MAGENTA + "[4] AutoMiner")
    print(Fore.RED + "[ESC] Salir\n" + Style.RESET_ALL)

while True:
    os.system('cls') 
    mostrar_menu()
    while True:
        if keyboard.is_pressed('1'):
            time.sleep(1)
            os.system('cls')
            print(Fore.GREEN + " Lanzando AutoClicker..." + Style.RESET_ALL)
            autoclicker()
            break
        elif keyboard.is_pressed('2'):
            print(Fore.GREEN + "\n Lanzando Farm Bot Simple..." + Style.RESET_ALL)
            farmBot()
            break
        elif keyboard.is_pressed('3'):
            print(Fore.GREEN + "\n Lanzando MobKiller..." + Style.RESET_ALL)
            mobKiller()
            break
        elif keyboard.is_pressed('4'):
            print(Fore.GREEN + "\n Lanzando autoMiner..." + Style.RESET_ALL)
            autoMiner()
            break
        elif keyboard.is_pressed('esc'):
            print(Fore.RED + "\n Saliendo del programa." + Style.RESET_ALL)
            
            exit()