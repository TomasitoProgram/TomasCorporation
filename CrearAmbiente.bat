@echo off


call python -m pip install --upgrade pip
call pip install --upgrade virtualenv
call python -m venv .venv
call .venv\Scripts\activate.bat

call python -m pip install --upgrade pip

call pip install pyautogui
call pip install keyboard
call pip install colorama
call pip install eel