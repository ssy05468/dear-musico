import pygame
import time

pygame.init()

WHITE = (255, 255, 255)
font = pygame.font.SysFont("comicsansms", 72)
text = font.render("Byrobot Python Piano", True, (0, 128, 0))

pyscreen = pygame.display.set_mode((1024, 768), 0, 32)
pyscreen.fill(WHITE)
pyscreen.blit(text, (512 - text.get_width() // 2, 384 - text.get_height() // 2))
pygame.display.flip()

run = True

pygame.mixer.init(44100,-16,2,8192)

a1 = pygame.mixer.Sound('a1.wav')
a1s = pygame.mixer.Sound('a1s.wav')
b1= pygame.mixer.Sound('b1.wav')
c1 = pygame.mixer.Sound('c1.wav')
c1s = pygame.mixer.Sound('c1s.wav')
c2 = pygame.mixer.Sound('c2.wav')
d1 = pygame.mixer.Sound('d1.wav')
d1s = pygame.mixer.Sound('d1s.wav')
e1 = pygame.mixer.Sound('e1.wav')
f1 = pygame.mixer.Sound('f1.wav')
f1s = pygame.mixer.Sound('f1s.wav')
g1 = pygame.mixer.Sound('g1.wav')
g1s = pygame.mixer.Sound('g1s.wav')

while run:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

            elif event.key == pygame.K_h:
                a1.play()

            elif event.key == pygame.K_u:
                a1s.play()

            elif event.key == pygame.K_j:
                b1.play()

            elif event.key == pygame.K_a:
                c1.play()

            elif event.key == pygame.K_w:
                c1s.play()

            elif event.key == pygame.K_s:
                d1.play()

            elif event.key == pygame.K_e:
                d1s.play()

            elif event.key == pygame.K_d:
                e1.play()

            elif event.key == pygame.K_f:
                f1.play()

            elif event.key == pygame.K_t:
                f1s.play()

            elif event.key == pygame.K_g:
                g1.play()

            elif event.key == pygame.K_y:
                g1s.play()

            elif event.key == pygame.K_k:
                c2.play()

pygame.quit()
