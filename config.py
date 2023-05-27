# Configurações do jogo
from os import path
import pygame

largura = 580
altura = 700
fps = 60

Imagens = path.join(path.dirname(__file__), 'assets', 'img')
Fontes = path.join(path.dirname(__file__), 'assets', 'fonts')
Botoes = path.join(path.dirname(__file__), 'assets', 'img', 'Botoes')
Beringuela = path.join(path.dirname(__file__), 'assets', 'img', 'Skins', 'beringuela')
Zedamanga = path.join(path.dirname(__file__), 'assets', 'img', 'Skins', 'zedamanga')

quit = 0
iniciando = 1
jogando = 2
skins = 3
instru = 4
# Cores principais

Roxo = (99,46,98)

