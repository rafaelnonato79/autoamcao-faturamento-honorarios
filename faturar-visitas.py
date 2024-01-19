#faturar visitas médicas em projetos

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
        #nova conta
        pyautogui.click(735,457,duration=0.2)
        pyautogui.press('enter')
        pyautogui.click(954,568)
        pyautogui.click(966,570)

        #mudanndo data de alta
        #copiar data de alta
        pyautogui.rightClick(822,526)
        pyautogui.click(911,597)
        #colar data de alta
        pyautogui.doubleClick(958,527,duration=0.2)
        pyautogui.hotkey('ctrl','v')

        #atualiza atendimento
        pyautogui.click(540,458,duration=0.2)
        time.sleep(0.5)

        #procedimento
        pyautogui.click(689,420,duration=0.2)
        pyautogui.write('20010')
        pyautogui.press('enter')
        pyautogui.write(valor)
        time.sleep(0.2)
        pyautogui.doubleClick(998,454)
        pyautogui.write('00')
        pyautogui.press('f3')

        pyautogui.click(729,658,duration=0.1)

        #voltar para dados da conta
        pyautogui.press('f6')

        #fechar conta
        time.sleep(0.3)
        pyautogui.click(1076,463,duration=0.1)
        pyautogui.press('enter')