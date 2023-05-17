# Configurações do jogo
from os import path
import pygame

largura = 580
altura = 700
fps = 60

window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Hello World!')

# ----- Inicia estruturas de dados
game = True

# ----- Inicia assets

imagem = pygame.image.load('PyGame-ClickerGame/Imagens/TelaInicial.png').convert()
imagem = pygame.transform.scale(imagem, (580, 700))

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(imagem, (0, 0))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados