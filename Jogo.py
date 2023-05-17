# O JOGO

import pygame
import os
from config import largura, altura, fps, iniciando, quit, jogando
from telainicial import telainicial
from telajogo import telajogo

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Navinha')

state = iniciando
while state != quit:
    if state == iniciando:
        state = telainicial(tela)
    elif state == jogando:
        state = telajogo(tela)
    else:
        state = quit

pygame.quit()