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
        self.image = pygame.transform.scale(img[0], tam)
        self.rect = self.image.get_rect()
        self.rect.centerx = largura/2
        self.rect.centery = (altura)/2-60

    def Botaoberi(self, screen, imagem, x, y):
        self.image = imagem[2]
        self.rect.x = x
        self.rect.y = y

        apertou = False

        pos = pygame.mouse.get_pos()


        if self.rect.collidepoint(pos):
            self.image = imagem[0]
            if pygame.mouse.get_pressed()[0] == True:
                apertou = True
                self.image = imagem[1]

        screen.blit(self.image, self.rect)  

        return apertou