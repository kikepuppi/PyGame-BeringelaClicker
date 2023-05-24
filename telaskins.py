# Tela das Skins de berinjela

from config import largura, altura, fps, quit, jogando, Roxo, skins
from assets import TelaI, TelaJ, TelaS, Selecionado, Selecionar, Comprar, Voltar, load_assets
from os import path
from classes import Button 
import pygame


tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Berijela Clicker')

assets = load_assets()[0]
btns = load_assets()[1]



# ----- Inicia estruturas de dados
def telaskins(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    Comprado1 = False
    Comprado2 = False
    Comprado3 = False
    Selecionar1 = 0
    Selecionar2 = 0
    Selecionar3 = 0
    Selecionado1 = 0
    Selecionado2 = 0
    Selecionado3 = 0
    Jacomprou1 = False
    Jacomprou2 = False
    Jacomprou3 = False

    botaoC1 = Button(((largura/2)+35),((altura/3)-40), btns[Comprar])
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
        

        # desenha botoes
    
        v = botaov.aparecer(screen, btns[Voltar])
        if Comprado1 == False:
            b1 = botaoC1.aparecer(screen, btns[Comprar])
        if Comprado2 == False:
            b2 = botaoC2.aparecer(screen, btns[Comprar])
        if Comprado3 == False:
            b3 = botaoC3.aparecer(screen, btns[Comprar])

        if Selecionar1 == 1:
            b1 = botaoS1.aparecer(screen, btns[Selecionar])
            Jacomprou1 = True
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
            
            if b1 and Jacomprou1 == False:
                Comprado1 = True
                Selecionar1 = 1
            if b2 and Jacomprou2 == False:
                Comprado2 = True
                Selecionar2 = 1
            if b3 and Jacomprou3 == False:
                Comprado3 = True
                Selecionar3 = 1
            if b1 and Jacomprou1 == True:
                Comprado1 = True
                Selecionar1 = 1
                Selecionado1 = 1
                Selecionado2 = 0
                Selecionado3 = 0
            if b2 and Jacomprou2 == True:
                Comprado2 = True
                Selecionar2 = 1
                Selecionado1 = 0
                Selecionado2 = 1
                Selecionado3 = 0
            if b3 and Jacomprou3 == True:
                Comprado3 = True
                Selecionar3 = 1
                Selecionado1 = 0
                Selecionado2 = 0
                Selecionado3 = 1



        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()


    return state