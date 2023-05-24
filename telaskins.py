# Tela das Skins de berinjela

from config import largura, altura, fps, quit, jogando, Roxo, skins
from assets import TelaI, TelaJ, TelaS, Selecionado, Selecionar, Comprar, Voltar, load_assets
from os import path
from classes import Button 
import pygame


tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Berigela Clicker')

assets = load_assets()[0]
btns = load_assets()[1]



# ----- Inicia estruturas de dados
def telaskins(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    Comprado = False
    Selecionado = False

    botaoC1 = Button(((largura/2)+35),((altura/3)-40), btns[Comprar])
    botaoC2 = Button(((largura/2)+35),((altura/3)+160), btns[Comprar])
    botaoC3 = Button(((largura/2)+35),((altura/3)+370), btns[Comprar])

    botaoS1 = Button(((largura/2)+35),((altura/3)-40), btns[Selecionar])
    botaoS2 = Button(((largura/2)+35),((altura/3)+160), btns[Selecionar])
    botaoS3 = Button(((largura/2)+35),((altura/3)+370), btns[Selecionar])

    estado_botoes = {
    botaoC1: 'comprar', 
    botaoC2: 'comprar',
    botaoC3: 'comprar'
}


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
        
        for botao, estado in estado_botoes.items():
            if estado == 'comprar':
                if botao.aparecer(screen, btns[Comprar]):
                    # Botão foi clicado, atualiza o estado para 'selecionar'
                    estado_botoes[botao] = 'selecionar'
            elif estado == 'selecionar':
                botao.aparecer(screen, btns[Selecionar])
                if botao.aparecer(screen, btns[Selecionar]):
                 # Botão foi clicado, atualiza o estado para 'selecionar'
                    estado_botoes[botao] = 'selecionado'
            elif estado == 'selecionado':
                botao.aparecer(screen, btns[Selecionado])
                
            
        
        v = botaov.aparecer(screen, btns[Voltar])
        
        
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
                if event.key == pygame.K_LEFT:
                    state = jogando
                    running = False


        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()


    return state