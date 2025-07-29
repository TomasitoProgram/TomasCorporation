import pyautogui, keyboard, os, time, sys
from colorama import init, Fore, Style
from utilidades import barra_de_cargaVerde, simulacionCargaRapida, simulacionCarga

def autoMiner():
    init()
    os.system('cls')
    barra_de_cargaVerde()
    time.sleep(1)
    os.system('cls')

    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "╔══════════════════════════════════════╗")
    print("║           Minecraft AutoMiner        ║")
    print("╚══════════════════════════════════════╝" + Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT + "\nSigue las instrucciones:")   
    print(Fore.LIGHTYELLOW_EX + " Presiona [1] para activar el minado y avance automático.")
    print(" Presiona [2] para detener.")
    print(" Presiona [ESC] para volver al menú." + Style.RESET_ALL)

    while True:
        if keyboard.is_pressed('esc'):
            print(Fore.RED + Style.BRIGHT + "\n Tecla ESC detectada. Regresando al menú..." + Style.RESET_ALL)
            time.sleep(1)
            keyboard.clear_all_hotkeys()
            keyboard.unhook_all()
            return

        if keyboard.is_pressed('1'):
            print(Fore.YELLOW + Style.BRIGHT)
            simulacionCarga()
            print(Style.RESET_ALL)
            os.system('cls')
            print(Fore.YELLOW + "\n AutoMiner AFK activado. (Presiona [2] para detener o [ESC] para salir.)" + Style.RESET_ALL)

            # Mantener click y tecla W presionados
            pyautogui.mouseDown(button='left')
            pyautogui.keyDown('w')

            while True:
                
                if keyboard.is_pressed('2'):
                    pyautogui.mouseUp(button='left')
                    pyautogui.keyUp('w')
                    print(Fore.RED + "\n AutoMiner detenido. Puedes volver a activarlo con [1] o salir con [ESC]." + Style.RESET_ALL)
                    simulacionCargaRapida()
                    os.system('cls')
                    break

                if keyboard.is_pressed('esc'):
                    pyautogui.mouseUp(button='left')
                    pyautogui.keyUp('w')
                    print(Fore.GREEN + Style.BRIGHT + "\n Tecla ESC detectada. Regresando al menú..." + Style.RESET_ALL)
                    time.sleep(1)
                    keyboard.clear_all_hotkeys()
                    keyboard.unhook_all()
                    os.system('cls')
                    return

                time.sleep(0.05)  # evita sobrecargar CPU

        time.sleep(0.05)
