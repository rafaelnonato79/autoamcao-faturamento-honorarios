import time
import pyautogui

#pausar o programa no tempo determinado
from time import sleep

with open('exames.txt') as exames:
    for index, exame in enumerate(exames):

        partes = exame.split(";")

        procedimento = partes[0]
        valor= partes[1]


        #procedimento
        pyautogui.click(492,450)
        pyautogui.write(procedimento)
        pyautogui.press('enter')
        pyautogui.write(valor)

        #Profissional para patologia
        if index == 0:
            pyautogui.doubleClick(1072,485, duration=0.2)
            pyautogui.write('790')

        #tablea 00
        pyautogui.doubleClick(998,454)
        pyautogui.write('00')

        pyautogui.press('f3')
