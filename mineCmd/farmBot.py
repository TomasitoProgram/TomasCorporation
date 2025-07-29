import pyautogui, keyboard, os, time, sys
from colorama import init, Fore, Style
from utilidades import barra_de_cargaAzul, simulacionCargaRapida, simulacionCarga

def farmBot():
    init()
    os.system('cls')
    barra_de_cargaAzul()
    time.sleep(1)
    os.system('cls')

    print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "╔══════════════════════════════════════╗")
    print("║          Minecraft Farm Bot          ║")
    print("╚══════════════════════════════════════╝" + Style.RESET_ALL)
    print(Fore.WHITE + Style.BRIGHT + "\nSigue las intrucciones:")   
    print(Fore.CYAN + " Presiona [1] para activar el plantado automático.")
    print(" Presiona [2] para detener la acción.")
    print(" Presiona [ESC] para volver al menú." + Style.RESET_ALL)

    while True:
        if keyboard.is_pressed('esc'):
            print(Fore.LIGHTRED_EX + Style.BRIGHT + "\n Tecla ESC detectada. Regresando al menú..." + Style.RESET_ALL)
            time.sleep(1)
            keyboard.clear_all_hotkeys()
            keyboard.unhook_all()
            return

        if keyboard.is_pressed('1'):
            print(Fore.CYAN + Style.BRIGHT)
            simulacionCarga()
            print(Style.RESET_ALL)
            os.system('cls')
            print(Fore.CYAN + "\n FarmBot activado. (Presiona [2] para detener o [ESC] para salir.)" + Style.RESET_ALL)

            while True:
                if keyboard.is_pressed('2'):
                    print(Fore.LIGHTYELLOW_EX + "\n FarmBot detenido. Puedes volver a activarlo con [1] o salir con [ESC]." + Style.RESET_ALL)
                    simulacionCargaRapida()
                    os.system('cls')
                    break

                if keyboard.is_pressed('esc'):
                    print(Fore.LIGHTRED_EX + Style.BRIGHT + "\n Tecla ESC detectada. Regresando al menú..." + Style.RESET_ALL)
                    time.sleep(1)
                    keyboard.clear_all_hotkeys()
                    keyboard.unhook_all()
                    os.system('cls')
                    return

                # Acción de plantado o uso alterno con clic derecho
                pyautogui.click(button='right')
                time.sleep(0.6)

        time.sleep(0.05)
