# Tela Inicial

from config import largura, altura, fps, quit, jogando, Roxo, instru
from assets import TelaI, load_assets
from os import path
import pygame


tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Berigela Clicker')


assets = load_assets()[0]

# ----- Inicia estruturas de dados
def telainicial(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    fundo = assets[TelaI]
    fundo_rect = fundo.get_rect()

    running = True
    keysdown = {}
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(fps)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = quit
                running = False

            if event.type == pygame.KEYDOWN:
                keysdown[event.key] = True
                
            if event.type == pygame.KEYUP and keysdown[event.key]:
                if event.key == pygame.K_t:
                    state = instru
                    running = False
                else:
                    state = jogando
                    running = False
                    
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(Roxo)
        screen.blit(fundo, fundo_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state