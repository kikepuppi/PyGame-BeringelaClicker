# Tela das Skins de berinjela

# Importa e Inicia pacotes
from config import font, largura, altura, fps, quit, jogando, Roxo, Branco, skins, Fontes, Imagens, Beringuela, Zedamanga
from assets import TelaI, TelaJ, TelaS, Selecionado, Selecionar, Comprar, Voltar, load_assets
from os import path
from classes import Button 
import pygame
import json

# Gera tela das Skins
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Berijela Clicker')


# ----- Inicia estruturas de dados
def telaskins(screen):
    
    assets = load_assets()[0]
    btns = load_assets()[1]
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Lê o que está inserido no arquivo save.json (goods)
    with open('save.json', 'r') as arquivo_json:
        texto = arquivo_json.read()
    goods = json.loads(texto)

    # Posicao das skins e textos
    pos1 = [[90, 185], [225, 185]]
    pos2 = [[90, 393.33], [235, 393.33]]
    pos3 = [[90, 603.33], [240, 593.33], [240, 613.33]]

    # Gera desenho das Skins e o Texto de seus nomes
    def templateSkin(arquivo, pos, nome):
        beri = pygame.image.load(path.join(Imagens, arquivo)).convert_alpha()
        beri = pygame.transform.scale(beri, (190, 190))
        beriRect = beri.get_rect()
        beriRect.center = pos[0]

        text = font.render(nome[0], True, Branco)
        textRect = text.get_rect()
        textRect.center = pos[1]

        if len(pos) == 3:
            text2 = font.render(nome[1], True, Branco)
            text2Rect = text2.get_rect()
            text2Rect.center = pos[2]
            return beri, beriRect, text, textRect, text2, text2Rect
        else:
            return beri, beriRect, text, textRect, None, None

    beri1,beri1Rect,textberi,textberiRect,_,_ = templateSkin('beri.png',pos1,['BERI'])
    beri2,beri2Rect,textberinguela,textberinguelarect,_,_ = templateSkin('beringuela.png',pos2,['BERINGUELA'])
    beri3,beri3Rect,textze,textzerect,textmanga,textmangarect = templateSkin('zedamanga.png',pos3,['ZE', 'DA MANGA'])

    # Lê o que está inserido no arquivo save.json (skins)
    with open('skin.json', 'r') as arquivo_json:
        texto1 = arquivo_json.read()
    
    # Transforma string em dicionário
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

    # Lê o que está inserido no arquivo save.json
    with open('save.json', 'r') as arquivo_json:
        texto = arquivo_json.read()
    goods = json.loads(texto)
    money = goods['Dinheiro']
    soma = goods['Soma']
    dima = goods['Gemas']
    Up1 = goods['Up1']
    Up2 = goods['Up2']
    Up3 = goods['Up3']
    Up4 = goods['Up4']
    Up5 = goods['Up5']
    Up6 = goods['Up6']
    Auto = goods['Auto']
    i = goods['Missao']
    clicks = goods['Clicks']
    acumulado = goods['Acumulado']
    acumuladoauto = goods['AcumuladoAuto']

    # Cria os Botões (Comprar, Selecionar e Selecionado)
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

        # Desenha textos, skins e nome das skins
        textdima = font.render(str(dima), True, Branco)
        textdimaRect = textdima.get_rect()
        textdimaRect.x = 465
        textdimaRect.y = 20
        screen.blit(textdima,textdimaRect)
        screen.blit(beri1, beri1Rect)
        screen.blit(beri2, beri2Rect)
        screen.blit(beri3, beri3Rect)
        screen.blit(textberi, textberiRect)
        screen.blit(textberinguela, textberinguelarect)
        screen.blit(textze, textzerect)
        screen.blit(textmanga, textmangarect)


        # Desenha botoes
        v = botaov.aparecer(screen, btns[Voltar])

        # Condição para caso haja skin que tenha sido comprada e selecionada e o jogador compre e selecione outra, a skin antes selecionada passa a ter a opção de selecionar e a que estava antes para selecionar agora está selecionada
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

            if v and event.type == pygame.MOUSEBUTTONUP:
                state = jogando
                running = False

            if b2 and Jacomprou2 == False and dima >= 5000 and event.type == pygame.MOUSEBUTTONUP:
                Comprado2 = True
                Selecionar2 = 1
                dima -= 5000
            if b3 and Jacomprou3 == False and dima >= 15000 and event.type == pygame.MOUSEBUTTONUP:
                Comprado3 = True
                Selecionar3 = 1
                dima -= 15000
            if b1 and Jacomprou1 == True and event.type == pygame.MOUSEBUTTONUP:
                Selecionado1 = 1
                Selecionado2 = 0
                Selecionado3 = 0
            if b2 and Jacomprou2 == True and event.type == pygame.MOUSEBUTTONUP:
                Comprado2 = True
                Selecionado1 = 0
                Selecionado2 = 1
                Selecionado3 = 0
            if b3 and Jacomprou3 == True and event.type == pygame.MOUSEBUTTONUP:
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

    # Define dicionário
    save = {'Dinheiro':money, 'Soma':soma,'Gemas':dima, 'Up1': Up1, 'Up2': Up2, 'Up3': Up3, 'Up4': Up4, 'Up5': Up5, 'Up6': Up6, 'Auto': Auto, 'Missao': i, 'Clicks': clicks, 'Acumulado': acumulado, 'AcumuladoAuto': acumuladoauto}

    # Transformando de volta para JSON (texto)
    novo_save = json.dumps(save)

    # Salvando o arquivo
    with open('save.json', 'w') as arquivo_json:
        arquivo_json.write(novo_save)



    return state