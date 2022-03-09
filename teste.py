import pyautogui
from PIL import Image
import webbrowser
import time 
import sys

# while True: #Start loop
#     print (pyautogui.position())
#     time.sleep(1)

url = sys.argv[1]
isEqual = sys.argv[2]
isPlus = sys.argv[3]
isFirstHalf = sys.argv[4]
isHome = sys.argv[5]

webbrowser.get('google-chrome').open(url)
time.sleep(5)

# # CLICA NO LOGIN
pyautogui.click(3232, 222)
time.sleep(3)
# #  LOGAR
pyautogui.click(2244, 300, clicks=2)
pyautogui.typewrite("usuario")
time.sleep(1)
pyautogui.press("tab")
pyautogui.typewrite("senha")
time.sleep(1)
pyautogui.press("enter")
time.sleep(6)
# CLICA NO ESCANTEIOS
pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('images/ABA_ESCANTEIOS.png',confidence=0.7)))
time.sleep(3)
pyautogui.scroll(-8)
time.sleep(1)
# MOVE O MOUSE PARA O TITULO DA APOSTA
if isEqual.lower() == 'true':
    pyautogui.moveTo(pyautogui.center(pyautogui.locateOnScreen('images/RACE.png',confidence=0.7)))
    if isHome.lower() == 'true':
        pyautogui.moveRel(223, 76, duration=1)
    else:
        pyautogui.moveRel(487, 77, duration=1)
    
elif isPlus.lower() == 'true':
    if isFirstHalf.lower() == 'true':
        pyautogui.moveTo(pyautogui.center(pyautogui.locateOnScreen('images/PLUS_FIRST.png',confidence=0.7)))
    else:    
        pyautogui.moveTo(pyautogui.center(pyautogui.locateOnScreen('images/PLUS_SECOND.png',confidence=0.7)))
elif isFirstHalf.lower() == 'true':
    pyautogui.moveTo(pyautogui.center(pyautogui.locateOnScreen('images/LIMIT_FIRST.png',confidence=0.7)))
else:
    pyautogui.moveTo(pyautogui.center(pyautogui.locateOnScreen('images/LIMIT_SECOND.png',confidence=0.7))) 




## CLICA NA APOSTA
pyautogui.click()
time.sleep(1)
## REALIZA A APOSTA
pyautogui.click(2173, 1014)
pyautogui.typewrite("1")
time.sleep(1)
pyautogui.click(2475, 1005)


# while True: #Start loop
#     print (pyautogui.position())
#     time.sleep(1)