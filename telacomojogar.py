# Tela de instruções 

from config import largura, altura, fps, quit, jogando, Roxo, skins, instru, iniciando
from assets import TelaI, TelaJ, TelaS, TelaC, load_assets, Voltar
from classes import Button, Berinjela
from os import path
import pygame

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Berigela Clicker')


assets = load_assets()[0]
btns = load_assets()[1]

def telacomojogar(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    butao = Button(10,10,btns[Voltar])

    # Carrega o fundo da tela inicial

    fundo = assets[TelaC]
    fundo_rect = fundo.get_rect()

    running = True
    keysdown = {}

    while running:

        v = butao.aparecer(screen, btns[Voltar])

        # Ajusta a velocidade do jogo.
        clock.tick(fps)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = quit
                running = False
            if v:
                state = iniciando
                running = False

            if event.type == pygame.KEYDOWN:
                keysdown[event.key] = True
                
            if event.type == pygame.KEYUP and keysdown[event.key]:
                if event.key == pygame.K_BACKSPACE:
                    state = iniciando
                    running = False
        

                # A cada loop, redesenha o fundo e os sprites
        screen.fill(Roxo)
        screen.blit(fundo, fundo_rect)


        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()


    return state



