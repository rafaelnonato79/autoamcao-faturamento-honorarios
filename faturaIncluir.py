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
        pyautogui.press('f3')
        pyautogui.press('enter')

        #pesquisar procedimento
        pyautogui.click(945,453,duration=0.5)

        #codigo procedimento
        pyautogui.click(1231,290,duration=1)
        pyautogui.write('20010')

        #tb padrão
        pyautogui.click(1148,290,duration=0.2)
        pyautogui.write('ATUALIZAÇÃO UNIMED REDE ABERTA POL 2021')
        #40
        for i in range(40):
            pyautogui.press('down')
        pyautogui.press('enter')

        #incluir procedimento
        pyautogui.click(1021,320,duration=0.2)
        pyautogui.press('enter')
        pyautogui.press('enter')

        #fechar tela de inclusão
        pyautogui.click(1362,218,duration=0.2)

        #tabela padrão
        pyautogui.doubleClick(1025,454,duration=0.2)
        pyautogui.write('00')

        #valor
        pyautogui.doubleClick(1079,456,duration=0.2)
        pyautogui.write(valor)
        time.sleep(0.2)


        pyautogui.press('f3')

        pyautogui.click(729,658,duration=0.1)

        #voltar para dados da conta
        pyautogui.press('f6')

        #fechar conta
        pyautogui.click(1076,463,duration=0.1)
        pyautogui.press('enter')

