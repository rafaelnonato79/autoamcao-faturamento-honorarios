import time
import pyautogui

#pausar o programa no tempo determinado
from time import sleep

with open('consultas.txt') as consultas:
    for consulta in consultas:
        atendimento = consulta.split(";")[0]
        procedimento= consulta.split(";")[1]

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

        pyautogui.moveTo(725,527,duration=0.2)
        pyautogui.mouseDown()

        pyautogui.moveTo(792,529,duration=0.2)
        pyautogui.mouseUp()
        pyautogui.hotkey('ctrl','c')

        #colar data de alta
        pyautogui.doubleClick(958,527,duration=0.2)
        pyautogui.hotkey('ctrl','v')
        time.sleep(0.2)
        pyautogui.write('059')

        #atualiza atendimento
        pyautogui.click(540,458,duration=0.2)
        time.sleep(1)

        #procedimento
        pyautogui.click(689,420,duration=0.2)
        time.sleep(0.5)
        pyautogui.doubleClick(492,450,duration=0.2)
        pyautogui.write(procedimento)
        time.sleep(0.2)

        #tabela padrão
        pyautogui.doubleClick(998,454,duration=0.2)
        pyautogui.write('00')

        #Profissional para patologia
        pyautogui.doubleClick(1072,485, duration=0.2)
        pyautogui.write('742')

        pyautogui.press('f3')

        pyautogui.click(729,658,duration=0.2)

        #voltar para dados da conta
        pyautogui.press('f6')

        #fechar conta
        time.sleep(0.3)
        pyautogui.click(1076,463,duration=0.1)
        time.sleep(0.2)
        pyautogui.press('enter')
        time.sleep(2)

        # #imprimir a conta
        # pyautogui.click(1072,321,duration=0.5)
        # time.sleep(1)
        # pyautogui.press('enter')
        # time.sleep(1)
        # pyautogui.click(224,38,duration=1)

        # #fechar conta
        # time.sleep(2)
        # pyautogui.hotkey('alt','f4')
        # time.sleep(2)

