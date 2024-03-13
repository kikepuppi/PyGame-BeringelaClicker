# Tela Jogando

from config import largura, altura, fps, quit, jogando, skins, Roxo, Fontes, Imagens, fim, SomFundo
from assets import TelaI, TelaJ, TelaS, load_assets, Upgrade, Beri, BSkins
from os import path
from classes import Button, Berinjela
import pygame
import json
from missoes import listamissoes

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Berijela Clicker')

pygame.font.init()
font = pygame.font.Font((path.join(Fontes, 'Valorax-lg25V.otf')),22)
font2 = pygame.font.Font((path.join(Fontes, 'Valorax-lg25V.otf')),9)
font3 = pygame.font.Font((path.join(Fontes, 'Valorax-lg25V.otf')),12)

# ----- Inicia estruturas de dados
def telajogo(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    moneyfoto = pygame.image.load(path.join(Imagens, 'money.png')).convert_alpha()
    moneyfoto = pygame.transform.scale(moneyfoto, (28, 28))
    moneyfotoRect = moneyfoto.get_rect()
    moneyfotoRect.center = (((largura/2)-1),365)

    assets = load_assets()[0]
    btns = load_assets()[1]

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
    now = 0
    ultimo = 0
    zerou = 0
    mant = 0
    magr = 0
    mps = 0

    running = True

    keysdown = {}
    while running:
        now = pygame.time.get_ticks() - ultimo
        if now >= 1000:
            money += int(Auto)
            magr += int(Auto)
            mps = magr-mant
            mant = magr
            now = 0
            ultimo = pygame.time.get_ticks()
            acumuladoauto += int(Auto)

        # Define o preco dos upgrades
        preco1 = int(10*(1.5**(Up1)))
        preco2 = int(1000*(1.1**(Up2)))
        preco3 = int(10000*(5.5**(Up3)))
        preco4 = int(50000*(1.1**(Up4)))
        preco5 = int(100000*(1.5**(Up5)))
        preco6 = int(500000000)

        # Importa a lista de missoes e determina a atual
        missoes = listamissoes(Up1,Up2,Up4,Up5,clicks,acumuladoauto,acumulado)
        missao_atual = missoes[i]
        nome_missao = missao_atual[0]
        check = missao_atual[1]
        complete = missao_atual[2]

        # Missao completa
        if check >= complete and i <= 20:
            i += 1
            dima += 1000
            clicks = 0
            acumulado = 0
            acumuladoauto = 0
        
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(Roxo)
        screen.blit(fundo, fundo_rect)

        # Escreve textos (Dineiro, mossoes, upgrades)
        branco = (255,255,255)
        textmoney = font.render(('{0:.2f}'.format(money)), True, branco)
        textmoneyRect = textmoney.get_rect()
        textmoneyRect.x = 60
        textmoneyRect.y = 20
        textdima = font.render(str(dima), True, branco)
        textdimaRect = textdima.get_rect()
        textdimaRect.x = 465
        textdimaRect.y = 20
        textnomemissao = font2.render(nome_missao, True, branco)
        textnomemissaoRect = textnomemissao.get_rect()
        textnomemissaoRect.center = (430,80)
        textqnt = font2.render(('{0:.0f}/{1}'.format(check, complete)), True, branco)
        textqntRect = textqnt.get_rect()
        textqntRect.center = (430,100)

        textUP1, textUP1Rect, textP1, textP1Rect = formatoPreco1(Up1, preco1, branco, (150,465), 40)

        textUP2, textUP2Rect, textP2, textP2Rect = formatoPreco1(Up2, preco2, branco, (150,570), 100)

        textUP3, textUP3Rect, textP3, textP3Rect = formatoPreco1(Up3, preco3, branco, (150,675), 4)

        textUP4, textUP4Rect, textP4, textP4Rect = formatoPreco2(Up4, preco4, branco, (440,465), 15)

        textUP5, textUP5Rect, textP5, textP5Rect = formatoPreco2(Up5, preco5, branco, (440,570), 15)

        textUP6 = font2.render(('{0}/{1}'.format(Up6, 1)), True, branco)
        textUP6Rect = textUP6.get_rect()
        textUP6Rect.center = (440,655)
        textP6 = font3.render(('$500 M'), True, branco)
        textP6Rect = textP6.get_rect()
        textP6Rect.center = (440,675)
        textseg = font.render(('{0:.2f}/s'.format(mps)), True, branco)
        textsegRect = textseg.get_rect()
        textsegRect.center = (largura/2-15,363)

        # Coloca textos na tela
        screen.blit(textmoney,textmoneyRect)
        screen.blit(textdima,textdimaRect)
        screen.blit(textnomemissao,textnomemissaoRect)
        screen.blit(textqnt,textqntRect)
        screen.blit(textUP1,textUP1Rect)
        screen.blit(textP1,textP1Rect)
        screen.blit(textUP2,textUP2Rect)
        screen.blit(textP2,textP2Rect)
        screen.blit(textUP3,textUP3Rect)
        screen.blit(textP3,textP3Rect)
        screen.blit(textUP4,textUP4Rect)
        screen.blit(textP4,textP4Rect)
        screen.blit(textUP5,textUP5Rect)
        screen.blit(textP5,textP5Rect)
        screen.blit(textUP6,textUP6Rect)
        screen.blit(textP6,textP6Rect)
        screen.blit(textseg,textsegRect)

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

            # Verifica se a berinjela foi clicada
            if beri and event.type == pygame.MOUSEBUTTONUP:
                money += int(soma)
                acumulado += int(soma)
                magr += int(soma)
                clicks += 1
            
            # Verifica se o botao Skins foi apertado
            if butskins and event.type == pygame.MOUSEBUTTONUP:
                state = skins
                running = False
            
            # Verifica se o botao Upgrade 1 foi apertado
            if up1 and money >= preco1 and Up1 < 40 and event.type == pygame.MOUSEBUTTONUP:
                Up1 += 1
                money = int(money-preco1)
                soma += 1

            # Verifica se o botao Upgrade 2 foi apertado
            if up2 and money >= preco2 and Up2 < 100 and event.type == pygame.MOUSEBUTTONUP:
                Up2 += 1
                money = int(money-preco2)
                Auto += 10
                money += Auto

            # Verifica se o botao Upgrade 3 foi apertado
            if up3 and money >= preco3 and Up3 < 4 and event.type == pygame.MOUSEBUTTONUP:
                Up3 += 1
                money = int(money-preco3)
                soma *= 1.15
                Auto *= 1.15

            # Verifica se o botao Upgrade 4 foi apertado
            if up4 and money>= preco4 and Up4 < 100 and event.type == pygame.MOUSEBUTTONUP:
                Up4 += 1
                money = int(money-preco4)
                Auto += 500

            # Verifica se o botao Upgrade 5 foi apertado
            if up5 and money >= preco5 and Up5 < 15 and event.type == pygame.MOUSEBUTTONUP:
                Up5 += 1
                money = int(money-preco5)
                soma += 100

            # Verifica se o botao Upgrade 6 foi apertado
            if up6 and money >= preco6 and Up6 < 1 and event.type == pygame.MOUSEBUTTONUP:
                Up6+=1
                money = int(money-preco6)
                zerou = 1
                Auto += 1000000

            # Verifica se zerou o jogo
            if zerou > 0:
                state = fim
                zerou = 0
                running = False

      

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        pygame.display.update()


    save(money, soma, dima, Up1, Up2, Up3, Up4, Up5, Up6, Auto, i, clicks, acumulado, acumuladoauto)

    return state

def formatoPreco2(Up4, preco4, branco, pos, size):
    textUP4 = font2.render(('{0}/{1}'.format(Up4, size)), True, branco)
    textUP4Rect = textUP4.get_rect()
    textUP4Rect.center = (pos[0],pos[1]-20)
    textP4 = font3.render(('${0:.1f}'.format(preco4)), True, branco)
    if preco4 >= 1000:
        textP4 = font3.render(('${0:.1f} mil'.format(preco4/1000)), True, branco)
        if preco4 >= 1000000:
            textP4 = font3.render(('${0:.1f} M'.format(preco4/1000000)), True, branco)
            if preco4 >= 1000000000:
                textP4 = font3.render(('${0:.1f} B'.format(preco4/1000000000)), True, branco)
    textP4Rect = textP4.get_rect()
    textP4Rect.center = pos
    return textUP4,textUP4Rect,textP4,textP4Rect

def formatoPreco1(Up, preco, branco, pos, size):
    textUP = font2.render(('{0}/{1}'.format(Up, size)), True, branco)
    textUPRect = textUP.get_rect()
    textUPRect.center = (pos[0],pos[1]-20)
    textP = font3.render(('${0:.1f}'.format(preco)), True, branco)
    if preco >= 1000:
        textP = font3.render(('${0:.1f} mil'.format(preco/1000)), True, branco)
        if preco >= 1000000:
            textP = font3.render(('${0:.1f} M'.format(preco/1000000)), True, branco)
    textPRect = textP.get_rect()
    textPRect.center = pos
    return textUP,textUPRect,textP,textPRect

def save(money, soma, dima, Up1, Up2, Up3, Up4, Up5, Up6, Auto, i, clicks, acumulado, acumuladoauto):
    save = {'Dinheiro':money, 'Soma':soma,'Gemas':dima, 'Up1': Up1, 'Up2': Up2, 'Up3': Up3, 'Up4': Up4, 'Up5': Up5, 'Up6': Up6, 'Auto': Auto, 'Missao': i, 'Clicks': clicks, 'Acumulado': acumulado, 'AcumuladoAuto': acumuladoauto}

    # Transformando de volta para JSON (texto)
    novo_save = json.dumps(save)

    # Salvando o arquivo
    with open('save.json', 'w') as arquivo_json:
        arquivo_json.write(novo_save)

