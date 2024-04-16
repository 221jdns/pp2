import pygame
import sys
import datetime
pygame.init()   

screen = pygame.display.set_mode((829, 836))
clock = pygame.image.load('mikki.png')
second = pygame.image.load('seconds.png')
minute = pygame.image.load('minute.png')
center = (415, 418)

def hands(current_time):
    second_angle = - current_time.second * 6
    minute_angle = - current_time.minute * 6
    rotated_second_hand = pygame.transform.rotate(second, second_angle)
    rotated_minute_hand = pygame.transform.rotate(minute, minute_angle)
    second_rect = rotated_second_hand.get_rect(center=center)
    minute_rect = rotated_minute_hand.get_rect(center=center)
    screen.blit(clock, (0, 0))
    screen.blit(rotated_second_hand, second_rect.topleft)
    screen.blit(rotated_minute_hand, minute_rect.topleft)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        current_time = datetime.datetime.now()
        hands(current_time)


    pygame.display.flip()
    pygame.time.delay(1000)


