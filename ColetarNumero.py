# Desenvolvido por Cadus
#  Importando todas as bibliotecas necessarias
from random import *
import pyautogui
import time
# Definindo DDD do numero
dd = '86'
# Alterando a pagina para a do whatsapp - atenção antes de executar deixe a pagina do zap aberta para poder alternar para ela
pyautogui.hotkey('alt','tab')

# loop infinito
while True:
    #gerando numero aleatorios no intervaldo de numeros existente no estado que moro
    numero = randint(81000000,99999999)
    numero = str(numero)
    numero = dd+numero
    pyautogui.PAUSE = 1
    pyautogui.click('ad.PNG')
    pyautogui.write(numero)
    pyautogui.press('enter')
    time.sleep(0.5)
    #verificando se o numero existe - caso ele existir não irá aparecer a mensagem na tela
    if pyautogui.locateOnScreen('ok.PNG'):
        pyautogui.click('ok.PNG')
    else:
        #salvando o numero ne um documento de texto
        with open('numeros.txt','a') as arquivo:
            arquivo.write(str(numero) + '\n')