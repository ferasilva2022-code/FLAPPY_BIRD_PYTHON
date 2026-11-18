import pygame
import os
import random

#--- CONSTANTES ---
#TELA
X = 500
Y = 800
TELA =(X,Y)

#IMAGENS PARA O JOGO
IMAGENS={
    'BACKGROUND':pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png'))),
    'CANO':pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png'))),
    'CHAO':pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png'))),
    'PASSARO': [
        pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))) ,
        pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))) ,
        pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png'))) 
    ]
}

#FONTE PARA O TEXTO E PONTUAÇÃO
pygame.font.init()
FONTE_PONTOS= pygame.font.SysFont('arial',50)


# --- OBJETOS DO JOGO ---
class Passaro:
    IMGS = IMAGENS['PASSARO']
    #animações
    ROTACAO = {
        'MAXIMA': 25,
        'VELOCIDADE':20
    }
    TEMPO_ANIMACAO = 5

    def __init__(self,x,y):
        self.x = x
        self.y = y
        # Funçaõ que cria o passaro
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem=0
        self.imagem_padrao = self.IMGS[0]

        #Função de pular
    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y

        #função para mover o passaro
    def mover(self):
        #calculo do deslocamento
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo**2) + self.velocidade * self.tempo #Fórmula do Sorvetão

        #restição do deslocamento
        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento <0 :
            deslocamento -=2

        self.y +=deslocamento

        #angulo do passaro
        if deslocamento < 0 or self.y < (self.altura+50):
            if self.angulo < self.ROTACAO['MAXIMA']:
                self.angulo = self.ROTACAO['MAXIMA']
            else:
                if self.angulo > -90:
                    self.angulo -= self.ROTACAO['VELOCIDADE']

    def desenhar(self,tela):
        #Definição das imagens do passaro (batidas de asa)
        self.contagem_imagem +=1
        if self.contagem_imagem < self.TEMPO_ANIMACAO:
            self.imagem_padrao = self.IMGS[0]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*2:
            self.imagem_padrao = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*3:
            self.imagem_padrao = self.IMGS[2]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*4:
            self.imagem_padrao=self.IMGS[1]
        elif self.contagem_imagem >= self.TEMPO_ANIMACAO*4+1:
            self.imagem_padrao= self.IMGS[0]
            self.contagem_imagem = 0


        #Passaro em queda, ou seja, não vai bater asa
        if self.angulo <= -80:
            self.imagem_padrao = self.IMGS[1]
            self.contagem_imagem = self.TEMPO_ANIMACAO*2


        # desenhar a imagem
        imagem_rotacionada = pygame.transform.rotate(self.imagem_padrao, self.angulo)
        posicao_central_imagem = self.get_rect(topleft=(self.x,self.y)).center
        retangle = imagem_rotacionada.get_rect(center=posicao_central_imagem)

        tela.blit(imagem_rotacionada, retangle.topleft)

        #Colisão com objetos na tela, vulgo canos.
        def get_mask(self):
          pygame.mask.from_surface(self.imagem_padrao)  
          #Aqui finaliza o esquema do passaro do jogo.


class Cano:
    pass

class Chao:
    pass