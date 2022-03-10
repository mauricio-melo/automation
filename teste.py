import pyautogui
import webbrowser
import time 
import sys

url = sys.argv[1]
isEqual = sys.argv[2]
isPlus = sys.argv[3]
isFirstHalf = sys.argv[4]
isHome = sys.argv[5]

# while True: #Start loop
#     print (pyautogui.position())
#     time.sleep(1)

webbrowser.get('google-chrome').open(url)
time.sleep(5)

# # CLICA NO LOGIN
pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('images/LOGIN.png',confidence=0.7)))
# pyautogui.click(3232, 222)
time.sleep(3)
# #  LOGAR
pyautogui.typewrite("F#carioca7")
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
pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('images/VALOR_APOSTA.png',confidence=0.7)))
pyautogui.typewrite("1")
time.sleep(1)

try:
    pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('images/FAZER_APOSTA.png',confidence=0.7)))
except:
    pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('images/ACEITAR_E_FAZER_APOSTA.png',confidence=0.7)))


# while True: #Start loop
#     print (pyautogui.position())
#     time.sleep(1)