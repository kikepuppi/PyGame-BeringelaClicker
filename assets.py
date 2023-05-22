# Imagens, Sons, Fontes, Entre outros

import pygame
import os
from config import largura, altura, Imagens

TelaI = 'Tela Inicial'
TelaJ = 'Tela Jogo'
TelaS = 'Tela Skins'
Voltar1 = 'Botão de Voltar 1'
Voltar2 = 'Botão de Voltar 2'
Comprar1 = 'Botão de Comprar 1'
Comprar2 = 'Botão de Comprar 2'
Interrogacao1 = 'Botão de Interrogação 1'
Interrogacao2 = 'Botão de Interrogação 2'
LoadGame1 = 'Botão de Load Game 1'
LoadGame2 = 'Botão de Load Game 2'
NewGame1 = 'Botão de New Game 1'
NewGame2 = 'Botão de New Game 2'
Selecionado1 = 'Botão de Selecionado 1'
Selecionado2 = 'Botão de Selecionado 2'
Selecionar1 = 'Botão de Selecionar 1'
Selecionar2 = 'Botão de Selecionar 2'
Skins1 = 'Botão de Skins 1'
Skins2 = 'Botão de Skins 2'
Upgrade1 = 'Botão de Upgrade 1'
Upgrade2 = 'Botão de Upgrade 2'

def load_assets():
    assets = {}
    assets[TelaI] = pygame.image.load(os.path.join(Imagens, 'TelaInicial.png')).convert()
    assets[TelaI] = pygame.transform.scale(assets[TelaI], (largura, altura))
    assets[TelaJ] = pygame.image.load(os.path.join(Imagens, 'TelaJogo.png')).convert()
    assets[TelaJ] = pygame.transform.scale(assets[TelaJ], (largura, altura))
    assets[TelaS] = pygame.image.load(os.path.join(Imagens, 'TelaSkins.png')).convert()
    assets[TelaS] = pygame.transform.scale(assets[TelaS], (largura, altura))
    assets[Comprar1] = pygame.image.load(os.path.join(Imagens, 'TelaSkins.png')).convert()
    assets[TelaS] = pygame.transform.scale(assets[TelaS], (largura, altura))
    assets[TelaS] = pygame.image.load(os.path.join(Imagens, 'TelaSkins.png')).convert()
    assets[TelaS] = pygame.transform.scale(assets[TelaS], (largura, altura))
    assets[TelaS] = pygame.image.load(os.path.join(Imagens, 'TelaSkins.png')).convert()
    assets[TelaS] = pygame.transform.scale(assets[TelaS], (largura, altura))
    assets[TelaS] = pygame.image.load(os.path.join(Imagens, 'TelaSkins.png')).convert()
    assets[TelaS] = pygame.transform.scale(assets[TelaS], (largura, altura))
    assets[TelaS] = pygame.image.load(os.path.join(Imagens, 'TelaSkins.png')).convert()
    assets[TelaS] = pygame.transform.scale(assets[TelaS], (largura, altura))
    assets[TelaS] = pygame.image.load(os.path.join(Imagens, 'TelaSkins.png')).convert()
    assets[TelaS] = pygame.transform.scale(assets[TelaS], (largura, altura))
    assets[TelaS] = pygame.image.load(os.path.join(Imagens, 'TelaSkins.png')).convert()
    assets[TelaS] = pygame.transform.scale(assets[TelaS], (largura, altura))
    assets[TelaS] = pygame.image.load(os.path.join(Imagens, 'TelaSkins.png')).convert()
    assets[TelaS] = pygame.transform.scale(assets[TelaS], (largura, altura))
    assets[TelaS] = pygame.image.load(os.path.join(Imagens, 'TelaSkins.png')).convert()
    assets[TelaS] = pygame.transform.scale(assets[TelaS], (largura, altura))

    return assets