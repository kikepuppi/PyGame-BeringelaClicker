# Tela Inicial

from config import largura, altura, fps, quit, jogando, Roxo, instru
from assets import TelaI, load_assets, Beri, Voltar, Interrogacao, NewGame, LoadGame
from os import path
import pygame
from classes import Button, Berinjela
import json 

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Berijela Clicker')


assets = load_assets()[0]
btns = load_assets()[1]

# criando a berinjela

beri = Berinjela(assets[Beri], (300,300))


# ----- Inicia estruturas de dados
def telainicial(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    
    assets = load_assets()[0]
    btns = load_assets()[1]

    # Carrega o fundo da tela inicial
    fundo = assets[TelaI]
    fundo_rect = fundo.get_rect()

    running = True
    keysdown = {}

    botaoint = Button(((largura/2)-25),600,btns[Interrogacao])
    botaonew = Button(((largura/2)-225), 470, btns[NewGame])
    botaoload = Button(((largura/2)+25), 470, btns[LoadGame])

    while running:

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(Roxo)
        screen.blit(fundo, fundo_rect)
        screen.blit(beri.image, beri.rect)

        int = botaoint.aparecer(screen, btns[Interrogacao])
        new = botaonew.aparecer(screen, btns[NewGame])
        load = botaoload.aparecer(screen, btns[LoadGame])

        # Ajusta a velocidade do jogo.
        clock.tick(fps)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = quit
                running = False

            if int:
                state = instru
                running = False
            
            if new:
                state = jogando
                running = False
            # Transformando de volta para JSON (texto)
                save = {'Dinheiro': 0, "Gemas": 0, 'Up1': 0, 'Up2': 0, 'Up3': 0, 'Up4': 0, 'Up5': 0, 'Up6': 0}
                skins = {'Comprado2': False, 'Comprado3': False, 'Selecionar1': 0, 'Selecionar2': 0, 'Selecionar3': 0, 'Selecionado1':1, 'Selecionado2':0, 'Selecionado3':0, 'Jacomprou1':True,'Jacomprou2':False,'Jacomprou3':False }
                novo_save = json.dumps(save)
                novo_skins = json.dumps(skins)
                # Salvando o arquivo
                with open('save.json', 'w') as arquivo_json:
                    arquivo_json.write(novo_save)
                with open('skin.json', 'w') as arquivo_json:
                    arquivo_json.write(novo_skins)
            if load:
                state = jogando
                running = False

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        pygame.display.update()
    return state