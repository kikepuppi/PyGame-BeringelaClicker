# Tela Jogando

from config import largura, altura, fps, quit, jogando, skins, Roxo
from assets import TelaI, TelaJ, TelaS, load_assets, Upgrade, Beri, BSkins
from os import path
from classes import Button, Berinjela
import pygame


tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Berigela Clicker')


assets = load_assets()[0]
btns = load_assets()[1]

# ----- Inicia estruturas de dados
def telajogo(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    fundo = assets[TelaJ]
    fundo_rect = fundo.get_rect()

    # Prepara os botoes.
    xeup = (largura/2)-95
    xdup = (largura/2)+xeup

    botaoup1 = Button(xeup,434,btns[Upgrade])
    botaoup2 = Button(xeup,540,btns[Upgrade])
    botaoup3 = Button(xeup,646,btns[Upgrade])
    botaoup4 = Button(xdup,434,btns[Upgrade])
    botaoup5 = Button(xdup,540,btns[Upgrade])
    botaoup6 = Button(xdup,646,btns[Upgrade])
    botaoberi = Berinjela(assets[Beri], (200,200))
    botaoskins = Button(10,65,btns[BSkins])

    running = True
    keysdown = {}
    while running:
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(Roxo)
        screen.blit(fundo, fundo_rect)

        # Desenha botoes de Upgrade.
        up1 = botaoup1.aparecer(screen, btns[Upgrade])
        up2 = botaoup2.aparecer(screen, btns[Upgrade])
        up3 = botaoup3.aparecer(screen, btns[Upgrade])
        up4 = botaoup4.aparecer(screen, btns[Upgrade])
        up5 = botaoup5.aparecer(screen, btns[Upgrade])
        up6 = botaoup6.aparecer(screen, btns[Upgrade])
        beri = botaoberi.Botaoberi(screen, assets[Beri], ((largura/2)-100), ((altura/2)-200))
        butskins = botaoskins.aparecer(screen, btns[BSkins])

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
                if event.key == pygame.K_RIGHT:
                    state = skins
                    running = False

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()


    return state