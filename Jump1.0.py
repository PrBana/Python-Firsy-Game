import math
import pygame

#https://humberto.io/pt-br/blog/desbravando-o-pygame-5-movimento-e-colisao/

WIDTH, HEIGHT = 900, 768    
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Jogo Do Espaço!')

POSITION_X = 0
square = pygame.Rect(300, 230, 20, 20)
left_pad = pygame.Rect(20, 210, 20, 60)
right_pad = pygame.Rect(600, 210, 20, 60)

pads = [left_pad, right_pad]

velocity_x = 0.1

#ASTRO = pygame.image.load( 'floating-astronaut-nasa.png')

PI = 3.141592653
WHITE = [255,255,255]
BLACK = [0,0,0]

FPS = 30


def draw_window_fix(dt, velocity_x, pads, square):
    WINDOW.fill(BLACK)

    X=0;Y=719; width = 900; height = 100; startAngle=0; endAngle=2*math.pi/2; linewidth = 50
    pygame.draw.arc(WINDOW, WHITE, (X,Y,width,height),startAngle,endAngle, linewidth)

    # usa a função move inplace
    square.move_ip(velocity_x * dt, 0)

    # checa por colisão com os pads
    if square.collidelist(pads) >= 0:
        velocity_x = -velocity_x

    pygame.draw.rect(WINDOW, WHITE, square)
    for pad in pads:
        pygame.draw.rect(WINDOW, WHITE, pad)

    pygame.display.flip()
    pygame.display.update()
    


def window(velocity_x, pads, square):
    clock = pygame.time.Clock()
    dt = clock.tick(30)
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        


        draw_window_fix(dt, velocity_x, pads, square)

    pygame.quit()

window(velocity_x, pads, square)

if __name__ == '__main__':
    window(velocity_x, pads, square)