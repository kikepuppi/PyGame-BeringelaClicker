# Tela de instruções 

# Imports
from config import largura, altura, fps, quit, jogando, Roxo, skins, instru, iniciando
from assets import TelaI, TelaJ, TelaS, TelaC, load_assets, Voltar
from classes import Button, Berinjela
from os import path
import pygame

# Gera a tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Berigela Clicker')

# Carrega os assets
assets = load_assets()[0]
btns = load_assets()[1]

def telacomojogar(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    botaov = Button(10,10,btns[Voltar])

    # Carrega o fundo da tela inicial

    fundo = assets[TelaC]
    fundo_rect = fundo.get_rect()

    running = True
    keysdown = {}

    while running:

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(Roxo)
        screen.blit(fundo, fundo_rect)

        # desenha botoes
        v = botaov.aparecer(screen, btns[Voltar])

        # Ajusta a velocidade do jogo.
        clock.tick(fps)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = quit
                running = False
            # Verifica se clicou para voltar
            if v:
                state = iniciando
                running = False
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()


    return state