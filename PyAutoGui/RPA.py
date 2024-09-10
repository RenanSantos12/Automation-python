
import pyautogui
import time
from turtle import position

position = pyautogui.position()
print(position)

pyautogui.alert('não use nada no seu computador')
pyautogui.PAUSE = 2
pyautogui.press('winleft')

pyautogui.write('crome')
pyautogui.press('enter')

time.sleep(1)
pyautogui.write('https://web.whatsapp.com/')
pyautogui.press('enter')
time.sleep(8)

#posição do mouse para arrastra o aqurivo 
pyautogui.hotkey('winleft', 'd')
pyautogui.moveTo(408,26)
pyautogui.mouseDown()
pyautogui.moveTo(545,361)
pyautogui.hotkey('alt', 'tab')
pyautogui.moveTo(252,396)
pyautogui.mouseUp()
pyautogui.press('enter')

#Point(x=283, y=325)


'''pyautogui.moveTo(283, 325)
pyautogui.mouseDown(button='right')
time.sleep(1)
pyautogui.write('Entrei nesse conversa para mandar oi')
time.sleep(2)
pyautogui.press('enter')'''