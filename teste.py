import pyautogui
import webbrowser
import time 
import sys

url = sys.argv[1]
isEqual = sys.argv[2]
isPlus = sys.argv[3]
isFirstHalf = sys.argv[4]
isHome = sys.argv[5]

def mouse_position():
    while True: #Start loop
        print (pyautogui.position())
        time.sleep(1)

def open_chrome():
    webbrowser.get('google-chrome').open(url)
    time.sleep(5)

def login():
    pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('images/LOGIN.png',confidence=0.7)))
    time.sleep(3)
    pyautogui.typewrite("F#carioca7")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(6)

def corner_tab():
    pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('images/ABA_ESCANTEIOS.png',confidence=0.7)))
    time.sleep(3)
    pyautogui.scroll(-8)
    time.sleep(1)      

def select_bet():
    if isEqual.lower() == 'true':
        pyautogui.moveTo(pyautogui.center(pyautogui.locateOnScreen('images/RACE.png',confidence=0.7)))
        if isHome.lower() == 'true':
            pyautogui.moveRel(223, 76, duration=1)
        else:
            pyautogui.moveRel(487, 77, duration=1)
    # elif isPlus.lower() == 'true':
    #     if isFirstHalf.lower() == 'true':
    #         pyautogui.moveTo(pyautogui.center(pyautogui.locateOnScreen('images/PLUS_FIRST.png',confidence=0.7)))
    #     else:    
    #         pyautogui.moveTo(pyautogui.center(pyautogui.locateOnScreen('images/PLUS_SECOND.png',confidence=0.7)))
    # elif isFirstHalf.lower() == 'true':
    #     pyautogui.moveTo(pyautogui.center(pyautogui.locateOnScreen('images/LIMIT_FIRST.png',confidence=0.7)))
    # else:
    #     pyautogui.moveTo(pyautogui.center(pyautogui.locateOnScreen('images/LIMIT_SECOND.png',confidence=0.7))) 
    pyautogui.click()
    time.sleep(1)

def make_bet():
    pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('images/VALOR_APOSTA.png',confidence=0.7)))
    pyautogui.typewrite("1")
    time.sleep(1)

    try:
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('images/FAZER_APOSTA.png',confidence=0.7)))
    except:
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('images/ACEITAR_E_FAZER_APOSTA.png',confidence=0.7)))


# mouse_position()
open_chrome()
login()
corner_tab()
select_bet()
make_bet()