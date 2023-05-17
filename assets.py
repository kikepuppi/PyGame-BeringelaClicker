# Imagens, Sons, Fontes, Entre outros

import pygame
import os
from config import largura, altura, Imagens

TelaI = 'Tela Inicial'

def load_assets():
    assets = {}
    assets['Tela Inicial'] = pygame.image.load(os.path.join(Imagens, 'TelaInicial.png')).convert()
    return assets