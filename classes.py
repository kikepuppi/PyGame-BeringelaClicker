# Classes
from config import largura, altura
import pygame

class Button():
    
    def __init__(self, x, y, imagem):
        self.image = imagem[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
     
    def aparecer(self, screen, imagem):

        apertou = False

        pos = pygame.mouse.get_pos()


        if self.rect.collidepoint(pos):
            self.image = imagem[1]

            if pygame.mouse.get_pressed()[0] == True:
                apertou = True


        if self.rect.collidepoint(pos) == False:
            self.image = imagem[0]


        screen.blit(self.image, self.rect)  

        return apertou
    
class Berinjela(pygame.sprite.Sprite):
    def __init__(self, img, tam):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img[0]
        self.image = pygame.transform.scale(self.image, tam)
        self.rect = self.image.get_rect()
        self.rect.centerx = largura/2
        self.rect.centery = (altura)/2-60
        self.i = 0
        self.last_update = 0

    def Botaoberi(self, screen, imagem, x, y):
        # Verifica o tick atual.
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update
        self.rect.x = x
        self.rect.y = y
        apertou = False

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos) == False:
            self.image = imagem[2]
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == True and elapsed_ticks > 20:
                apertou = True
                self.i += 1
                if self.i % 2 == 1:
                    self.image = imagem[0]
                elif self.i % 2 == 0:
                    self.image = imagem[1]
                self.last_update = pygame.time.get_ticks()
        pygame.time.delay(50)
        screen.blit(self.image, self.rect)  

        return apertou