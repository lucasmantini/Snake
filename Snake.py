import pygame, random
from pygame.locals import * #Importante para capturar os eventos do jogo.

def alinhamento(): #Alinhar a comida com a cobrinha, padronizando as posições de 10 pixels.
    x = random.randint(0, 990)
    y = random.randint(0, 590)
    return(x//10 * 10, y//10 * 10)

def colisao_maca(c1, c2): #Teste de colisão entre objetos.
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

def colisao_borda(c1): #Teste de colisão com as bordas da tela.
    return (True if c1[0] == 1000 or c1[1] == 600
            or c1[0] < 0 or c1[1] < 0 else False)

def colisao_corpo(c1, snake): #Teste de colisão com partes do próprio corpo.
    
    return False

#Direções da cobrinha.
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

pygame.init()
pygame.font.init()

#O jogo foi pensado para dividir os componentes em quadrados de 10x10 pixels.
tela = pygame.display.set_mode((1000, 650))#Tela do jogo (funciona como uma matriz).
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

direcao = 10 #Direção inicial da cobrinha.

fps = pygame.time.Clock() #Objeto para controlar o fps do jogo.
vel = 5 #Velocidade do fps.

pontuacao = pygame.font.SysFont('Comic Sans MS', 18) #Definir fonte de escrita na tela.
pontos = 0 #Contagem de pontos.

while True:#Laço necessário para o funcionamneto do jogo.
    fps.tick(vel)

    for event in pygame.event.get():#Caputar os eventos do jogo (apertar teclas, por exemplo).
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        if event.type == KEYDOWN:#Eventos de pressionar as teclas para controlar a cobrinha.
            if event.key == K_UP and direcao != DOWN:
                direcao = UP
            if event.key == K_DOWN and direcao != UP:
                direcao = DOWN
            if event.key == K_LEFT and direcao != RIGHT:
                direcao = LEFT
            if event.key == K_RIGHT and direcao != LEFT:
                direcao = RIGHT
    
    if colisao_borda(snake[0]):
       break
    
    for i in range(1, len(snake) - 1): #Teste de colisão com partes do corpo.
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
           break  
    
    if colisao_maca(snake[0], pos_comida): 
        pos_comida = alinhamento() #Gera nova comida.
        snake.append((0, 0)) #Aumenta a cobrinha.
        pontos += 1
        vel = (vel + 1 if vel <= 30 and (pontos%5 == 0) else vel)

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

    pygame.draw.line(tela, (255, 255, 255), (0, 610), (1000, 610))

    #Criar score na tela.
    pont_text = pontuacao.render("Score: " + str(pontos), True, (255, 255, 255)) 
    pont_rect = pont_text.get_rect()
    pont_rect.topleft = (1000 - 120, 615)
    tela.blit(pont_text, pont_rect)

    for pos in snake:
        tela.blit(corpo, pos)
        #A função blit é responsável por plotar a imagem na tela de jogo, recebendo como
        #argumentos a imagem a ser plotada e a posição. Surface é a classe responsável
        #por manipular objetos na superfície da tela de jogo.

    pygame.display.update()#Atualizar a tela do jogo.

while True: #Tela final.
    tela.fill((0, 0, 0))
    pont_text = pygame.font.SysFont('Comic Sans MS', 30).render("GAME OVER", True, (255, 255, 255)) 
    pont_rect = pont_text.get_rect()
    pont_rect.midtop = (500, 250)
    tela.blit(pont_text, pont_rect)
    pont_text = pontuacao.render("Total: " + str(pontos), True, (255, 255, 255)) 
    pont_rect = pont_text.get_rect()
    pont_rect.midtop = (500, 310)
    tela.blit(pont_text, pont_rect)
    pygame.display.update()
    pygame.time.wait(1000)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()