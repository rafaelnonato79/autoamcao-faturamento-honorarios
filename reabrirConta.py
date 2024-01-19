import time
import pyautogui

#pausar o programa no tempo determinado
from time import sleep

imagemAlerta = 'alerta.png'
with open('visitas.txt') as visitas:
    for visita in visitas:
        atendimento = visita.split(";")[0]
        valor= visita.split(";")[1]
        
        pyautogui.doubleClick(518,468,duration=0.5)
        pyautogui.write(atendimento)
        pyautogui.press('enter')
        time.sleep(1)
        
        #reabrir conta
        pyautogui.click(821,455,duration=0.2)
        time.sleep(0.5)
        pyautogui.click(482,491,duration=0.2)
        pyautogui.write(' ')
        pyautogui.click(711,484,duration=0.2)
        pyautogui.press('enter')
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.click(689,420,duration=0.2)
        time.sleep(1)
        pyautogui.press('f5')
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(0.2)
        pyautogui.press('f6')
        time.sleep(0.2)
        pyautogui.click(1035,672,duration=0.2)
        pyautogui.press('enter')