import pygame, random
from pygame.locals import * #Importante para capturar os eventos do jogo.

def alinhamento(): #Alinhar a comida com a cobrinha, padronizando as posições de 10 pixels.
    x = random.randint(0, 990)
    y = random.randint(0, 590)
    return(x//10 * 10, y//10 * 10)

def colisao_maca(c1, c2): #Teste de colisão entre objetos.
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

def colisao_borda(c1, tela): #Teste de colisão com as bordas da tela.
    return (c1[0] == tela[0]) and (c1[1] == tela[1])

def colisao_corpo(): #Teste de colisão com partes do próprio jogo.
    return()

#Direções da cobrinha.
UP = 0
DOWN = 1
RIGHT = 3
LEFT = 2

pontos = 0 #Contagem de pontos.

pygame.init()

#O jogo foi pensado para dividir os componentes em quadrados de 10x10 pixels.
tela = pygame.display.set_mode((1000, 600))#Tela do jogo (funciona como uma matriz).
pygame.display.set_caption('Snake')#Título da tela.

snake = [(300, 300),(310, 300),(320, 300)]
#A cobrinha é representada por uma lista de posições onde se encontra no plano da tela.
corpo = pygame.Surface((10,10))
corpo.fill((255, 255, 255))
#Preencher o corpo da cobrinha e colorir.

pos_comida = alinhamento()
comida = pygame.Surface((10, 10))
comida.fill((255, 2, 3))
#Criar e colorir a comida da cobrinha.

direcao = LEFT #Direção inicial da cobrinha.

fps = pygame.time.Clock()
#Objeto para controlar o fps do jogo.

while True:#Laço necessário para o funcionamneto do jogo.
    fps.tick(30)

    for event in pygame.event.get():#Caputar os eventos do jogo (apertar teclas, por exemplo).
        if event.type == QUIT:
            pygame.quit()
        
        if event.type == KEYDOWN:#Eventos de pressionar as teclas para controlar a cobrinha.
            if event.key == K_UP:
                direcao = UP
            if event.key == K_DOWN:
                direcao = DOWN
            if event.key == K_LEFT:
                direcao = LEFT
            if event.key == K_RIGHT:
                direcao = RIGHT
    
    if colisao_borda(snake[0], tela):
        pygame.init()
        tela_final = pygame.display.set_mode((320, 240))#Tela de fim de jogo.
        pygame.display.set_caption('Resultado Final')#Título da tela.
        tela_final.blit(pontos, (160, 120))

    if colisao_maca(snake[0], pos_comida): 
        pos_comida = alinhamento() #Gera nova comida.
        snake.append((0, 0)) #Aumenta a cobrinha.
        pontos += 1

    #Movimentos da cobrinha a partir da "cabeça".
    if direcao == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if direcao == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if direcao == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if direcao == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])
    #Movimentação do corpo da cobrinha.

    tela.fill((0, 0, 0))#"Limpar" a tela de jogo.
    tela.blit(comida, pos_comida)#Plotar a comida na tela.

    for pos in snake:
        tela.blit(corpo, pos)
        #A função blit é responsável por plotar a imagem na tela de jogo, recebendo como
        #argumentos a imagem a ser plotada e a posição. Surface é a classe responsável
        #por manipular objetos na superfície da tela de jogo.

    pygame.display.update()#Atualizar a tela do jogo.