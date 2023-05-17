# Imagens, Sons, Fontes, Entre outros

import pygame
import os
from config import largura, altura, Imagens

TelaI = 'Tela Inicial'
TelaJ = 'Tela Jogo'
def load_assets():
    assets = {}
    assets[TelaI] = pygame.image.load(os.path.join(Imagens, 'TelaInicial.png')).convert()
    assets[TelaJ] = pygame.image.load(os.path.join(Imagens, 'TelaJogo.png')).convert()
    assets[TelaJ] = pygame.transform.scale(assets[TelaJ], (largura, altura))

    return assets