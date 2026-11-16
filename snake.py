# CRÉDITOS: https://youtu.be/2PWEa2UgnDI?si=-jXKauoY0Jl0vk39
# Feito por: Fernanda Alves da Silva
# Objetivo: Treinar Python

import pygame
import random

pygame.init()
tela = pygame.display.set_mode((600,400)) # tamanho da tela
relogio = pygame.time.Clock()
TAMANHO_CELULA = 20 #tamanho dos quadrados
GRAMA=(162,209,73)

inicio=[
    pygame.Rect(x,200,TAMANHO_CELULA,TAMANHO_CELULA)
    for x in (80,60,40)
]
cobra = inicio.copy()
direcao = (1,0)
fruta = pygame.Rect(400,200,TAMANHO_CELULA,TAMANHO_CELULA)
pontos = 0
fonte = pygame.font.Font(None,40) #desenhar a pontuação na tela
setas = {
    pygame.K_LEFT: (-1,0), #esquerda
    pygame.K_RIGHT:(1,0), #direita
    pygame.K_UP: (0,-1), #cima
    pygame.K_DOWN: (0,1), #baixo
}

rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT: #quitando o game
            rodando = False
        elif evento.type == pygame.KEYDOWN:
            nova = setas.get(evento.key,direcao) #procura uma nova direção
            if nova !=(-direcao[0],-direcao[1]):
                direcao=nova
    dx,dy = direcao
    cabeca = cobra[0].move(dx*TAMANHO_CELULA, dy*TAMANHO_CELULA) #tamanho inicial
    fora = not tela.get_rect().contains(cabeca) 
    #Tipos de colisões
    if fora or cabeca.collidelist(cobra) >=0:
        cobra=inicio.copy()
        direcao= (1,0)
        pontos =0
        continue

    cobra.insert(0,cabeca) 
    #fazendo a cobra comer
    if cabeca == fruta:
        pontos +=1 #soma 1 a pontos
        #define as novas posições da frutinha
        x= random.randrange(0,600,TAMANHO_CELULA)
        y =random.randrange(40,400,TAMANHO_CELULA)
        fruta = pygame.Rect(x,y,TAMANHO_CELULA,TAMANHO_CELULA)
    else:
        cobra.pop()

    tela.fill((170,215,81))
    for x in range (0,600,TAMANHO_CELULA):
        for y in range(x % 40,400,40):
            celula = (x,y,TAMANHO_CELULA,TAMANHO_CELULA)
            pygame.draw.rect(tela,GRAMA,celula)
    #Placar
    placar= fonte.render(f'Pontos: {pontos}',1,'white')
    tela.blit(placar,(10,100)) #aparece la no canto esquerdo

    for parte in cobra:
        pygame.draw.rect(tela,'royalblue',parte,0,6) #cobrinha original, azul e com bordas arredondadas
    # desenhando a fruta
    pygame.draw.circle(tela, 'yellow', fruta.center, 9)
    
    pygame.display.flip()
    relogio.tick(10)





