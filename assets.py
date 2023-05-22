# Imagens, Sons, Fontes, Entre outros

import pygame
import os
from config import largura, altura, Imagens

TelaI = 'Tela Inicial'
TelaJ = 'Tela Jogo'
TelaS = 'Tela Skins'
Voltar1 = 'Botão de Voltar 1'
Voltar1 = 'Botão de Voltar 1'
Voltar1 = 'Botão de Voltar 1'
Voltar1 = 'Botão de Voltar 1'
Voltar1 = 'Botão de Voltar 1'
Voltar1 = 'Botão de Voltar 1'
Voltar1 = 'Botão de Voltar 1'
Voltar1 = 'Botão de Voltar 1'
Voltar1 = 'Botão de Voltar 1'
Voltar1 = 'Botão de Voltar 1'
Voltar1 = 'Botão de Voltar 1'
Voltar1 = 'Botão de Voltar 1'
Voltar1 = 'Botão de Voltar 1'
Voltar1 = 'Botão de Voltar 1'
Voltar1 = 'Botão de Voltar 1'
Voltar1 = 'Botão de Voltar 1'
Voltar1 = 'Botão de Voltar 1'
Voltar1 = 'Botão de Voltar 1'

def load_assets():
    assets = {}
    assets[TelaI] = pygame.image.load(os.path.join(Imagens, 'TelaInicial.png')).convert()
    assets[TelaI] = pygame.transform.scale(assets[TelaI], (largura, altura))
    assets[TelaJ] = pygame.image.load(os.path.join(Imagens, 'TelaJogo.png')).convert()
    assets[TelaJ] = pygame.transform.scale(assets[TelaJ], (largura, altura))
    assets[TelaS] = pygame.image.load(os.path.join(Imagens, 'TelaSkins.png')).convert()
    assets[TelaS] = pygame.transform.scale(assets[TelaS], (largura, altura))

    return assets