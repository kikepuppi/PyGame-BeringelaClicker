# O JOGO

import pygame
import os 
from config import largura, altura, fps, iniciando, quit, jogando, skins, instru 
from telainicial import telainicial
from telajogo import telajogo
from telaskins import telaskins
from telacomojogar import telacomojogar

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Berinjela Clicker')

state = iniciando
while state != quit:
    if state == iniciando:
        state = telainicial(tela)
    elif state == jogando:
        state = telajogo(tela)
    elif state == skins:
        state = telaskins(tela)
    elif state == instru:
        state = telacomojogar(tela)
    else:
        state = quit

pygame.quit()