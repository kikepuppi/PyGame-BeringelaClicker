# O JOGO

import pygame
import os
from config import largura, altura, fps, iniciando, quit
from telainicial import telainicial

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Navinha')

state = iniciando
while state != quit:
    if state == iniciando:
        state = telainicial(tela)