# Tela Jogando

from config import largura, altura, fps, quit, jogando, skins, Roxo, Fontes
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
font2 = pygame.font.Font((path.join(Fontes, 'Valorax-lg25V.otf')),10)
# ----- Inicia estruturas de dados
def telajogo(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

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

        preco1 = int(10*(1.5**(Up1)))
        preco2 = int(1000*(1.1**(Up2)))
        preco3 = int(10000*(5.5**(Up3)))
        preco4 = int(50000*(1.1**(Up4)))
        preco5 = int(100000*(1.5**(Up5)))
        preco6 = int(500000)

        missoes = listamissoes()
        missao_atual = missoes[i]
        nome_missao = missao_atual[0]
        check = missao_atual[1]
        complete = missao_atual[2]
        
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(Roxo)
        screen.blit(fundo, fundo_rect)

        textmoney = font.render(str(money), True, (255,255,255))
        textmoneyRect = textmoney.get_rect()
        textmoneyRect.x = 60
        textmoneyRect.y = 20
        textdima = font.render(str(dima), True, (255,255,255))
        textdimaRect = textdima.get_rect()
        textdimaRect.x = 465
        textdimaRect.y = 20
        textnomemissao = font2.render(nome_missao, True, (255,255,255))
        textnomemissaoRect = textnomemissao.get_rect()
        textnomemissaoRect.center = (430,80)
        textqnt = font2.render(('{0}/{1}'.format(check, complete)), True, (255,255,255))
        textqntRect = textqnt.get_rect()
        textqntRect.center = (430,100)


        screen.blit(textmoney,textmoneyRect)
        screen.blit(textdima,textdimaRect)
        screen.blit(textnomemissao,textnomemissaoRect)
        screen.blit(textqnt,textqntRect)

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
                money += soma
                
            if butskins:
                state = skins
                running = False
            
            if up1 and money >= preco1:
                Up1 += 1
                money = int(money-preco1)
                soma += 1
                if Up1 > 40:
                    Up1 -= 1

            if up2 and money >= preco2:
                Up2 += 1
                money = int(money-preco2)
                Auto += 1
                money += Auto
                if Up2 > 100:
                    Up2 -= 1

            if up3 and money >= preco3:
                Up3 += 1
                money = int(money-preco3)
                money *= 0.5
                if Up3 > 4:
                    Up3 -= 1

            if up4 and money>= preco4:
                Up4 += 1
                money = int(money-preco4)
                Auto += 100
                money += Auto
                if Up4> 100:
                    Up4 -= 1

            if up5 and money >= preco5:
                Up5 += 1
                money = int(money-preco5)
                soma += 10
                if Up5 >15:
                    Up5 -= 1

            if up6 and money >= preco6:
                Up6+=1
                money = int(money-preco6)
                #não sei oq faz (mudar a tela talvez?)
                if Up6 > 1:
                    Up6 -= 1 #(acho q isso não vai precisar se a funcionalidade for oq parece 
      

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        pygame.display.update()


    save = {'Dinheiro':money, 'Soma':soma,'Gemas':dima, 'Up1': Up1, 'Up2': Up2, 'Up3': Up3, 'Up4': Up4, 'Up5': Up5, 'Up6': Up6, 'Auto': Auto, 'Missao': i}

    # Transformando de volta para JSON (texto)
    novo_save = json.dumps(save)

    # Salvando o arquivo
    with open('save.json', 'w') as arquivo_json:
        arquivo_json.write(novo_save)

    return state