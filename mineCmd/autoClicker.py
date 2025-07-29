import pyautogui, keyboard, os, time, sys
from colorama import init, Fore, Style
from utilidades import barra_de_cargaMorado, simulacionCargaRapida,simulacionCarga

def autoclicker():
    init()
    os.system('cls')
    barra_de_cargaMorado()
    time.sleep(1)
    os.system('cls')

    print(Fore.LIGHTRED_EX + Style.BRIGHT + "╔══════════════════════════════════════╗")
    print("║         Minecraft AutoClicker        ║")
    print("╚══════════════════════════════════════╝" + Style.RESET_ALL)
    print(Fore.RED + Style.BRIGHT + "\nSigue las intrucciones:")   
    print(Fore.CYAN + " Presiona [1] para mantener el clic presionado.")
    print(" Presiona [2] para soltar el clic.")
    print(" Presiona [ESC] para volver al menú." + Style.RESET_ALL)

    while True:
        if keyboard.is_pressed('esc'):
            print(Fore.RED + Style.BRIGHT + "\n Tecla ESC detectada. Regresando al menú..." + Style.RESET_ALL)
            time.sleep(1)
            keyboard.clear_all_hotkeys()
            keyboard.unhook_all()
            return

        if keyboard.is_pressed('1'):
            print(Fore.RED + Style.BRIGHT)
            simulacionCarga()
            print(Style.RESET_ALL)
            time.sleep(1)
            os.system('cls')
            time.sleep(1.5)
            print(Fore.RED + "\n Acción para minar aplicada. (Presiona [2] para soltar o [ESC] para salir.)" + Style.RESET_ALL)
            pyautogui.mouseDown(button='left')

            while True:
                if keyboard.is_pressed('2'):
                    pyautogui.mouseUp(button='left')
                    simulacionCargaRapida()
                    os.system('cls')
                    print(Fore.YELLOW + " Clic liberado. Puedes volver a activarlo con [1] o [ESC] para volver al menú." + Style.RESET_ALL)
                    break
                if keyboard.is_pressed('esc'):
                    pyautogui.mouseUp(button='left')
                    print(Fore.GREEN + Style.BRIGHT + "\n Tecla ESC detectada. Regresando al menú..." + Style.RESET_ALL)
                    time.sleep(1)
                    keyboard.clear_all_hotkeys()
                    keyboard.unhook_all()
                    os.system('cls')
                    return
        time.sleep(0.05)
