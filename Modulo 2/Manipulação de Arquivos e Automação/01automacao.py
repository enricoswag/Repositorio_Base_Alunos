# 1° passo: instalar o pyautogui com o comndo:
# pip install pyautogui
#crie uma automação que automaticamente um navegador 

# importamos bibliotecas para o script o script em uso
import pyautogui
# 'press' é um comando que utilizou
# para pressionar a tecla desejada
pyautogui.press('Win') # para pressionar a tecla windows
#'SLEEP' é um comando que utilizamos para deixar o codigo 
# em espera por alguns segundos
pyautogui.sleep(1)

# 'write' e um comando que utilizamos escrever o que queremos escrever

pyautogui.write('Google chrome')

pyautogui.press('Enter')