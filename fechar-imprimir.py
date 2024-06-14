import time
import pyautogui

#pausar o programa no tempo determinado
from time import sleep

with open('atendimentos.txt') as atendimentos:
    for atendimento in atendimentos:
        
        pyautogui.doubleClick(518,468,duration=0.5)
        pyautogui.write(atendimento)
        pyautogui.press('enter')
        time.sleep(1)
        
         
        #  #fechar conta
        # time.sleep(0.3)
        # pyautogui.click(1076,463,duration=0.1)
        # time.sleep(0.2)
        # pyautogui.press('enter')

        #imprimir a conta
        pyautogui.click(1072,321,duration=0.5)
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(224,38,duration=1)

        #fechar conta 
        time.sleep(4)
        pyautogui.hotkey('alt','f4')
        time.sleep(3)