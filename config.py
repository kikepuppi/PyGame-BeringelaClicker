# Configurações do jogo
from os import path
import pygame


# Infos Básicas
largura = 580
altura = 700
fps = 60


# Paths para arquivos/pastas
Imagens = path.join(path.dirname(__file__), 'assets', 'img')
Fontes = path.join(path.dirname(__file__), 'assets', 'fonts')
Botoes = path.join(path.dirname(__file__), 'assets', 'img', 'Botoes')
Beringuela = path.join(path.dirname(__file__), 'assets', 'img', 'Skins', 'beringuela')
Zedamanga = path.join(path.dirname(__file__), 'assets', 'img', 'Skins', 'zedamanga')
SomFundo = path.join(path.dirname(__file__), 'assets', 'wav', 'music_a.mp3')
Click = path.join(path.dirname(__file__), 'assets', 'wav', 'Click.mp3')

# States
quit = 0
iniciando = 1
jogando = 2
skins = 3
instru = 4
intro = 5
fim = 6

# Cores principais

Roxo = (99,46,98)
Branco = (255,255,255)

# Fontes
pygame.font.init()
font = pygame.font.Font((path.join(Fontes, 'Valorax-lg25V.otf')),22)
font2 = pygame.font.Font((path.join(Fontes, 'Valorax-lg25V.otf')),9)
font3 = pygame.font.Font((path.join(Fontes, 'Valorax-lg25V.otf')),12)

# Funcoes
def templateUpgrade(quantidade, max, pos, preco):
    textUP = font2.render(('{0}/{1}'.format(quantidade, max)), True, Branco)
    textUPRect = textUP.get_rect()
    textUPRect.center = (pos)
    textP = font3.render(('${0:.1f}'.format(preco)), True, Branco)
    if preco >= 1000:
        textP = font3.render(('${0:.1f} mil'.format(preco/1000)), True, Branco)
    elif preco >= 1000000:
        textP = font3.render(('${0:.1f} M'.format(preco/1000000)), True, Branco)
    elif preco >= 1000000000:
        textP = font3.render(('${0:.1f} B'.format(preco/1000000000)), True, Branco)

    textPRect = textP.get_rect()
    textPRect.center = (pos[0], pos[1]+20)

    return textUP, textUPRect, textP, textPRect

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