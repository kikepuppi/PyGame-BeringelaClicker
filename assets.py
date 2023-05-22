# Imagens, Sons, Fontes, Entre outros

import pygame
import os
from config import largura, altura, Imagens, Botoes

TelaI = 'Tela Inicial'
TelaJ = 'Tela Jogo'
TelaS = 'Tela Skins'
TelaC = 'Tela Como Jogar'
Voltar = 'Botão de Voltar'
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
    assets[TelaC] = pygame.image.load(os.path.join(Imagens, 'TelaInstrucao.png')).convert()
    assets[TelaC] = pygame.transform.scale(assets[TelaC], (largura, altura))
    btns[Comprar] = [pygame.image.load(os.path.join(Botoes, 'Comprar1.png')).convert(),pygame.image.load(os.path.join(Botoes, 'Comprar2.png')).convert()]
    btns[Comprar] = pygame.transform.scale(assets[Comprar], (largura, altura))
    btns[Voltar] = [pygame.image.load(os.path.join(Botoes, 'Voltar1.png')).convert(),pygame.image.load(os.path.join(Botoes, 'Voltar2.png')).convert()]
    btns[Voltar] = pygame.transform.scale(assets[Voltar], (largura, altura))
    btns[Interrogacao] = [pygame.image.load(os.path.join(Botoes, 'Interrogacao1.png')).convert(),pygame.image.load(os.path.join(Botoes, 'Interrogacao2.png')).convert()]
    btns[Interrogacao] = pygame.transform.scale(assets[Interrogacao], (largura, altura))
    btns[LoadGame] = [pygame.image.load(os.path.join(Botoes, 'LoadGame1.png')).convert(),pygame.image.load(os.path.join(Botoes, 'LoadGame2.png')).convert()]
    btns[LoadGame] = pygame.transform.scale(assets[LoadGame], (largura, altura))
    btns[NewGame] = [pygame.image.load(os.path.join(Botoes, 'NewGame1.png')).convert(),pygame.image.load(os.path.join(Botoes, 'NewGame2.png')).convert()]
    btns[NewGame] = pygame.transform.scale(assets[NewGame], (largura, altura))
    btns[Selecionado] = [pygame.image.load(os.path.join(Botoes, 'Selecionado1.png')).convert(),pygame.image.load(os.path.join(Botoes, 'Selecionado2.png')).convert()]
    btns[Selecionado] = pygame.transform.scale(assets[Selecionado], (largura, altura))
    btns[Selecionar] = [pygame.image.load(os.path.join(Botoes, 'Selecionar1.png')).convert(),pygame.image.load(os.path.join(Botoes, 'Selecionar2.png')).convert()]
    btns[Selecionar] = pygame.transform.scale(assets[Selecionar], (largura, altura))
    btns[BSkins] = [pygame.image.load(os.path.join(Botoes, 'Skins1.png')).convert(),pygame.image.load(os.path.join(Botoes, 'Skins2.png')).convert()]
    btns[BSkins] = pygame.transform.scale(assets[BSkins], (largura, altura))
    btns[Upgrade] = [pygame.image.load(os.path.join(Botoes, 'Upgrade1.png')).convert(),pygame.image.load(os.path.join(Botoes, 'Upgrade2.png')).convert()]
    btns[Upgrade] = pygame.transform.scale(assets[Upgrade], (largura, altura))


    return [assets, btns]