import pygame

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280,720))
running = True

blue = 0
green = 0
a = +4

while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    blue += a
    green += a
    if blue >= 255 - a or blue < a:
        a *= -1

    pygame.draw.rect(screen,(135,206,235),(0,0,1280,720))
    pygame.draw.rect(screen,(0,255,0),(0,648,1280,72))
    pygame.draw.circle(screen,(255,green,0),(128,128),(128))

    pygame.draw.rect(screen,(0,255,0),(640,360,50,350))

    pygame.draw.circle(screen, (255,0,blue), (590,320), 50)
    pygame.draw.circle(screen, (255, 255, 0), (590, 320), 25)

    pygame.draw.circle(screen, (255, 0, blue), (665, 375), 50)
    pygame.draw.circle(screen, (255, 255, 0), (665, 375), 25)

    pygame.draw.circle(screen, (255, 0, blue), (665, 300), 50)
    pygame.draw.circle(screen, (255, 255, 0), (665, 300), 25)

    pygame.draw.circle(screen, (255, 0, blue), (740, 320), 50)
    pygame.draw.circle(screen, (255, 255, 0), (740, 320), 25)

    pygame.draw.circle(screen, (255, 0, blue), (610, 240), 50)
    pygame.draw.circle(screen, (255, 255, 0), (610, 240), 25)

    pygame.draw.circle(screen, (255, 0, blue), (700, 235), 50)
    pygame.draw.circle(screen, (255, 255, 0), (700, 235), 25)

    pygame.draw.ellipse(screen, (0, 255, 0) ,(675,500,100,50),50)
    pygame.draw.ellipse(screen, (0, 255, 0), (550,600, 100, 50), 50)


    clock.tick(60)
    pygame.display.flip()
