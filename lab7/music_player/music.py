import pygame
import sys
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600,300))
songs = ['HHA.mp3','WWW.mp3','HHP.mp3']
pygame.mixer.music.load(songs[0])
pygame.mixer.music.play()
current_song = songs[0]
i = 0
paused = False
font = pygame.font.Font(None, 36)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.exit
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                i = (i + 1)
                pygame.mixer.music.load(songs[i])
                pygame.mixer.music.play()
                current_song = songs[i]
            elif event.key == pygame.K_LEFT:
                i = (i - 1)
                pygame.mixer.music.load(songs[i])
                pygame.mixer.music.play()
                current_song = songs[i]
            elif event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True
    screen.fill((255, 255, 255))
    text = font.render("Now playing: " + current_song, True, (0, 0, 0))
    screen.blit(text, (20, 20))

    text2 = font.render("pause/play,", True, (0, 0, 0))
    screen.blit(text2, (20, 100))

    text3 = font.render("Previous song,", True, (0, 0, 0))
    screen.blit(text3, (20, 140))

    text4 = font.render("Next song", True, (0, 0, 0))
    screen.blit(text4, (20, 180))

    pygame.display.flip()
    clock.tick(60)

