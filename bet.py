import pyautogui
import webbrowser
import time 

def mouse_position():
    while True: 
        print (pyautogui.position())
        time.sleep(1)

def open_chrome(url):
    webbrowser.get('google-chrome').open(url)
    time.sleep(7)

def login(password):
    pyautogui.click(1883, 211)
    time.sleep(3)
    pyautogui.typewrite(password)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(6)

def corner_tab():
    pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('images/ABA_ESCANTEIOS.png',confidence=0.7)))
    time.sleep(3)
    pyautogui.scroll(-8)
    time.sleep(2)      

def select_bet(isEqual, isPlus, isFirstHalf, isHome):
    if isEqual.lower() == 'true':
        select_race(isHome)
    elif isPlus.lower() == 'true':
        select_plus(isFirstHalf)
    else:
        select_limit(isFirstHalf)
    pyautogui.click()
    time.sleep(1)

def select_race(isHome):
    pyautogui.moveTo(pyautogui.center(pyautogui.locateOnScreen('images/RACE.png',confidence=0.7)))
    if isHome.lower() == 'true':
        pyautogui.moveRel(223, 76, duration=1)
    else:
        pyautogui.moveRel(487, 77, duration=1)

def select_plus(isFirstHalf):
    if isFirstHalf.lower() == 'true':
        pyautogui.moveTo(pyautogui.center(pyautogui.locateOnScreen('images/PLUS_FIRST.png',confidence=0.7)))
    else:    
        pyautogui.moveTo(pyautogui.center(pyautogui.locateOnScreen('images/PLUS_SECOND.png',confidence=0.7)))

def select_limit(isFirstHalf):
    pyautogui.moveTo(pyautogui.center(pyautogui.locateOnScreen('images/LIMIT_SECOND.png',confidence=0.7)))
    if isFirstHalf.lower() == 'true':
        pyautogui.moveRel(203, 200, duration=1) 
    else:
        pyautogui.moveRel(223, 76, duration=1)             

def make_bet(money):
    pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('images/VALOR_APOSTA.png',confidence=0.7)))
    pyautogui.typewrite(money)
    time.sleep(1)
    try:
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('images/FAZER_APOSTA.png',confidence=0.7)))
    except:
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('images/ACEITAR_E_FAZER_APOSTA.png',confidence=0.7)))