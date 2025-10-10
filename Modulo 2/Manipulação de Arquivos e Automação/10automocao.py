#desenhar um objeto
# apos a execuçao de codigo abra um bloco de 
# notas para o desenho ser criado

import pyautogui
import time

pyautogui.press('win')
time.sleep(1)
pyautogui.write('bloco de notas')
pyautogui.press('enter')
time.sleep(2)
arvore = [
    '   ^    ',
    '  ^^^   ',
    ' ^^^^^  ',
    '  |||   ',
    '  |||   '
]
for linha in arvore:
    pyautogui.write(linha, interval=0.1)
    pyautogui.press('enter')
print('desenho da arvore concluido!')