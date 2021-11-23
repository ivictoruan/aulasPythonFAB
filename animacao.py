import pygame, time

# Setando cores:
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)

# Definindo dimensão da janela
LARGURAJ = 700
ALTURAJ = 700

janela = pygame.display.set_mode((LARGURAJ, ALTURAJ))

pygame.display.set_caption('Aula | Animação!')

# Uma figura pode ser definida pela seguinte sintaxe: figura = [tipo, cor, velocidade, forma]
f1 = [pygame.Rect(300, 80, 40, 80), VERMELHO, [0, -5], 'ELIPSE']
f2 = [pygame.Rect(200, 200, 20, 20), VERDE, [5, 5], 'ELIPSE']
f3 = [pygame.Rect(100, 150, 60, 60), AZUL, [-5, 5], 'RETANGULO']
f4 = [pygame.Rect(200, 150, 80, 40), AMARELO, [5,0], 'RETANGULO']

figuras = [f1, f2, f3, f4] # lista contendo as figuras criadas!

def mover(figura, dim_janela):
    borda_esquerda = 0
    borda_superior = 0
    borda_direita = dim_janela[0]
    borda_inferior = dim_janela[1]

    if figura[0].left < borda_esquerda or figura[0].right > borda_direita:
        figura[2][0] = - figura[2][0] # para o eixo x
    if figura[0].top < borda_superior or figura[0].bottom > borda_inferior:
        figura[2][1] = - figura[2][1] # para o eixo y

    figura[0].x += figura[2][0]
    figura[0].y += figura[2][1]


deve_continuar = True
while deve_continuar:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            deve_continuar = False
    janela.fill(PRETO)

    for figura in figuras:
        mover(figura, (LARGURAJ, ALTURAJ))
        if figura[3] == 'RETANGULO':
            pygame.draw.rect(janela, figura[1], figura[0])
            
        elif figura[3] == 'ELIPSE':
            pygame.draw.ellipse(janela, figura[1], figura[0])
        

    pygame.display.update() # Atualiza a janela de exibição!
    time.sleep(0.02)

pygame.quit()
