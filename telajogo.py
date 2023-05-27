# Tela Jogando

from config import largura, altura, fps, quit, jogando, skins, Roxo, Fontes
from assets import TelaI, TelaJ, TelaS, load_assets, Upgrade, Beri, BSkins
from os import path
from classes import Button, Berinjela
import pygame
import json




tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Berijela Clicker')

assets = load_assets()[0]
btns = load_assets()[1]
pygame.font.init()
font = pygame.font.Font((path.join(Fontes, 'Valorax-lg25V.otf')),22)
# ----- Inicia estruturas de dados
def telajogo(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    with open('save.json', 'r') as arquivo_json:
        texto = arquivo_json.read()
    goods = json.loads(texto)
    money = goods['Dinheiro']
    dima = goods['Gemas']
    Up1 = goods['Up1']
    Up2 = goods['Up2']
    Up3 = goods['Up3']
    Up4 = goods['Up4']
    Up5 = goods['Up5']
    Up6 = goods['Up6']
    # Carrega o fundo da tela inicial
    fundo = assets[TelaJ]
    fundo_rect = fundo.get_rect()
    # Prepara os botoes.
    xe = (largura/2)-95
    xd = (largura/2)+xe
    botaoup1 = Button(xe,434,btns[Upgrade])
    botaoup2 = Button(xe,540,btns[Upgrade])
    botaoup3 = Button(xe,646,btns[Upgrade])
    botaoup4 = Button(xd,434,btns[Upgrade])
    botaoup5 = Button(xd,540,btns[Upgrade])
    botaoup6 = Button(xd,646,btns[Upgrade])
    botaoberi = Berinjela(assets[Beri], (200,200))
    botaoskins = Button(10,65,btns[BSkins])

    running = True

    keysdown = {}
    while running:
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(Roxo)
        screen.blit(fundo, fundo_rect)

        textmoney = font.render(str(money), True, (255,255,255))
        textdima = font.render(str(dima), True, (255,255,255))
        textmoneyRect = textmoney.get_rect()
        textdimaRect = textdima.get_rect()
        textmoneyRect.x = 60
        textmoneyRect.y = 20
        textdimaRect.x = 465
        textdimaRect.y = 20


        screen.blit(textmoney,textmoneyRect)
        screen.blit(textdima,textdimaRect)

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
            if beri:
                money += 1

            if butskins:
                state = skins
                running = False
            
            if up1:
                Up1 += 1
            if up2:
                Up2 += 1
            if up3:
                Up3 += 1
            if up4:
                Up4 += 1
            if up5:
                Up5 += 1
            if up6:
                Up6 += 1
            

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        pygame.display.update()


    save = {'Dinheiro':money, 'Gemas':dima, 'Up1': Up1, 'Up2': Up2, 'Up3': Up3, 'Up4': Up4, 'Up5': Up5, 'Up6': Up6}

    # Transformando de volta para JSON (texto)
    novo_save = json.dumps(save)

    # Salvando o arquivo
    with open('save.json', 'w') as arquivo_json:
        arquivo_json.write(novo_save)

    return state