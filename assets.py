# Imagens, Sons, Fontes, Entre outros

import pygame
import os
from config import largura, altura, Imagens, Botoes

TelaI = 'Tela Inicial'
TelaJ = 'Tela Jogo'
TelaS = 'Tela Skins'
Voltar1 = 'Botão de Voltar 1'
Voltar2 = 'Botão de Voltar 2'
Comprar = 'Botão de Comprar'
Interrogacao = 'Botão de Interrogação'
LoadGame = 'Botão de Load Game'
NewGame = 'Botão de New Game'
Selecionado = 'Botão de Selecionado'
Selecionar = 'Botão de Selecionar'
BSkins = 'Botão de Skins'
Upgrade = 'Botão de Upgrade'


def load_assets():
    assets = {}
    btns = {}
    assets[TelaI] = pygame.image.load(os.path.join(Imagens, 'TelaInicial.png')).convert()
    assets[TelaI] = pygame.transform.scale(assets[TelaI], (largura, altura))
    assets[TelaJ] = pygame.image.load(os.path.join(Imagens, 'TelaJogo.png')).convert()
    assets[TelaJ] = pygame.transform.scale(assets[TelaJ], (largura, altura))
    assets[TelaS] = pygame.image.load(os.path.join(Imagens, 'TelaSkins.png')).convert()
    assets[TelaS] = pygame.transform.scale(assets[TelaS], (largura, altura))
    btns[Comprar] = pygame.image.load(os.path.join(Botoes, 'TelaSkins.png')).convert()
    btns[Comprar] = pygame.transform.scale(assets[TelaS], (largura, altura))
    btns[Interrogacao] = pygame.image.load(os.path.join(Botoes, 'TelaSkins.png')).convert()
    btns[Interrogacao] = pygame.transform.scale(assets[TelaS], (largura, altura))
    btns[LoadGame] = pygame.image.load(os.path.join(Botoes, 'TelaSkins.png')).convert()
    btns[LoadGame] = pygame.transform.scale(assets[TelaS], (largura, altura))
    btns[TelaS] = pygame.image.load(os.path.join(Botoes, 'TelaSkins.png')).convert()
    btns[TelaS] = pygame.transform.scale(assets[TelaS], (largura, altura))
    btns[TelaS] = pygame.image.load(os.path.join(Botoes, 'TelaSkins.png')).convert()
    btns[TelaS] = pygame.transform.scale(assets[TelaS], (largura, altura))
    btns[TelaS] = pygame.image.load(os.path.join(Botoes, 'TelaSkins.png')).convert()
    btns[TelaS] = pygame.transform.scale(assets[TelaS], (largura, altura))
    btns[TelaS] = pygame.image.load(os.path.join(Botoes, 'TelaSkins.png')).convert()
    btns[TelaS] = pygame.transform.scale(assets[TelaS], (largura, altura))
    btns[TelaS] = pygame.image.load(os.path.join(Botoes, 'TelaSkins.png')).convert()
    btns[TelaS] = pygame.transform.scale(assets[TelaS], (largura, altura))
    btns[TelaS] = pygame.image.load(os.path.join(Botoes, 'TelaSkins.png')).convert()
    btns[TelaS] = pygame.transform.scale(assets[TelaS], (largura, altura))

    return [assets, btns]