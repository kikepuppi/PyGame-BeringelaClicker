# Tela das Skins de berinjela

from config import largura, altura, fps, quit, jogando, Roxo, skins, Fontes
from assets import TelaI, TelaJ, TelaS, Selecionado, Selecionar, Comprar, Voltar, load_assets
from os import path
from classes import Button 
import pygame
import json


tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Berijela Clicker')

assets = load_assets()[0]
btns = load_assets()[1]
pygame.font.init()
font = pygame.font.Font((path.join(Fontes, 'Valorax-lg25V.otf')),22)


# ----- Inicia estruturas de dados
def telaskins(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    with open('save.json', 'r') as arquivo_json:
        texto = arquivo_json.read()
    goods = json.loads(texto)

    
    with open('skin.json', 'r') as arquivo_json:
        texto1 = arquivo_json.read()
    
    skinsdic = json.loads(texto1)
    goods = json.loads(texto)

    dima = goods['Gemas']

    Comprado2 = skinsdic['Comprado2']
    Comprado3 = skinsdic['Comprado3']
    Selecionar1 = skinsdic['Selecionar1']
    Selecionar2 = skinsdic['Selecionar2']
    Selecionar3 = skinsdic['Selecionar3']
    Selecionado1 = skinsdic['Selecionado1']
    Selecionado2 = skinsdic['Selecionado2']
    Selecionado3 = skinsdic['Selecionado3']
    Jacomprou1 = skinsdic['Jacomprou1']
    Jacomprou2 = skinsdic['Jacomprou2']
    Jacomprou3 = skinsdic['Jacomprou3']

    #botaoC1 = Button(((largura/2)+35),((altura/3)-40), btns[Comprar])
    botaoC2 = Button(((largura/2)+35),((altura/3)+160), btns[Comprar])
    botaoC3 = Button(((largura/2)+35),((altura/3)+370), btns[Comprar])

    botaoS1 = Button(((largura/2)+35),((altura/3)-40), btns[Selecionar])
    botaoS2 = Button(((largura/2)+35),((altura/3)+160), btns[Selecionar])
    botaoS3 = Button(((largura/2)+35),((altura/3)+370), btns[Selecionar])

    botaoSe1 = Button(((largura/2)+35),((altura/3)-40), btns[Selecionado])
    botaoSe2 = Button(((largura/2)+35),((altura/3)+160), btns[Selecionado])
    botaoSe3 = Button(((largura/2)+35),((altura/3)+370), btns[Selecionado])

    botaov = Button(10,10,btns[Voltar])

    # Carrega o fundo da tela inicial
    fundo = assets[TelaS]
    fundo_rect = fundo.get_rect()

    running = True
    keysdown = {}
    while running:
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(Roxo)
        screen.blit(fundo, fundo_rect)

        textdima = font.render(str(dima), True, (255,255,255))
        textdimaRect = textdima.get_rect()
        textdimaRect.center = (475,33)
        screen.blit(textdima,textdimaRect)

        # desenha botoes

        v = botaov.aparecer(screen, btns[Voltar])

        if Comprado2 == False:
            b2 = botaoC2.aparecer(screen, btns[Comprar])
        if Comprado3 == False:
            b3 = botaoC3.aparecer(screen, btns[Comprar])

        if Selecionado1 == 0:
            b1 = botaoS1.aparecer(screen, btns[Selecionar]) 
        
        if Selecionar2 == 1:
            b2 = botaoS2.aparecer(screen, btns[Selecionar])
            Jacomprou2 = True

        if Selecionar3 == 1:
            b3 = botaoS3.aparecer(screen, btns[Selecionar])
            Jacomprou3 = True

        if Selecionado1 == 1:   
            b1 = botaoSe1.aparecer(screen, btns[Selecionado]) 

        if Selecionado2 == 1:   
            b2 = botaoSe2.aparecer(screen, btns[Selecionado]) 

        if Selecionado3 == 1:   
            b3 = botaoSe3.aparecer(screen, btns[Selecionado])
        
        
        # Ajusta a velocidade do jogo.
        clock.tick(fps)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = quit
                running = False

            if v:
                state = jogando
                running = False

            if b2 and Jacomprou2 == False:
                Comprado2 = True
                Selecionar2 = 1
            if b3 and Jacomprou3 == False:
                Comprado3 = True
                Selecionar3 = 1
            if b1 and Jacomprou1 == True:
                Selecionado1 = 1
                Selecionado2 = 0
                Selecionado3 = 0
            if b2 and Jacomprou2 == True:
                Comprado2 = True
                Selecionado1 = 0
                Selecionado2 = 1
                Selecionado3 = 0
            if b3 and Jacomprou3 == True:
                Comprado3 = True
                Selecionar1 = 1
                Selecionado1 = 0
                Selecionado2 = 0
                Selecionado3 = 1



        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        pygame.display.update()

    skins = {'Comprado2': Comprado2, 'Comprado3': Comprado3, 'Selecionar1': Selecionar1, 'Selecionar2': Selecionar2, 'Selecionar3': Selecionar3, 'Selecionado1':Selecionado1, 'Selecionado2':Selecionado2, 'Selecionado3':Selecionado3, 'Jacomprou1':Jacomprou1,'Jacomprou2':Jacomprou3,'Jacomprou3':Jacomprou3 }

    # Transformando de volta para JSON (texto)
    novo_skins = json.dumps(skins)

    # Salvando o arquivo
    with open('skin.json', 'w') as arquivo_json:
        arquivo_json.write(novo_skins)



    return state