import pygame 
import sys
pygame.init()

display = pygame.display.set_mode((500,300))
ball_x = (500 - 25) // 2
ball_y = (300 - 25) // 2
run = True 
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if ball_y - 20>=0 + 25:
                    ball_y -=20
            elif event.key == pygame.K_DOWN:
                if ball_y + 20<=300 - 25:
                    ball_y +=20
            elif event.key == pygame.K_LEFT:
                if ball_x - 20>=0 + 25:
                    ball_x -=20
            elif event.key == pygame.K_RIGHT:
                if ball_x + 20<=500 -25:
                    ball_x +=20
                

    display.fill((255, 255, 255))
    pygame.draw.circle(display,(255,0,0), (ball_x, ball_y), (25))
    pygame.display.flip()

