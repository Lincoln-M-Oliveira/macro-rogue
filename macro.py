import pyautogui as pg
import pyperclip
import numpy as np
import time
import keyboard

def gatecheck():
    """
    Verifica se o menu do gate está aberto
    Faz uma captura de tela da região esperada e conta os pixels brancos (texto)
    Retorna true se o menu for detectado
    """
    img = pg.screenshot(region=(587, 185, 194, 40))
    img_array = np.array(img)
    mask_branco = (img_array[:,:,0] > 240) & (img_array[:,:,1] > 240) & (img_array[:,:,2] > 240) 
    return mask_branco.sum() > 350

def get_key_input(): 
    """
    Aguarda o jogador selecionar uma tecla de destino
    O menu do gate fecha após alguns segundos,
    então não é necessário tratar caso o jogador não escolha nada.
    """

    while True:
        if keyboard.is_pressed('1'):
            return 'sigil'
        elif keyboard.is_pressed('2'):
            return 'skycastle'
        elif keyboard.is_pressed('3'):
            return 'tundra'
        elif keyboard.is_pressed('4'):
            return 'desert'
        elif keyboard.is_pressed('5'):
            return 'deepforest'
        

def send_key_input(destino):
    """
    Copia o destino para área de transferência e envia para a textbox do jogo.
    Usa 'enter' pra abrir e fechar a textbox.
    """
    pyperclip.copy(destino)
    keyboard.send('enter')
    time.sleep(0.1)
    pg.hotkey('ctrl', 'v')
    time.sleep(0.1)
    keyboard.send('enter')

while True:
    """
    Caso detectado o menu do gate, roda a função keys() e espera o input do jogador
    Quando detecta input do player, copia e cola o destino na textbox do menu
    Também checa pela key "delete", caso queira fechar o script
    """
    if gatecheck():
        destino = get_key_input()
        send_key_input(destino)
        time.sleep(0.05) # Delay para consumir menos recursos

    if keyboard.is_pressed('delete'):
        print("break") 
        break
