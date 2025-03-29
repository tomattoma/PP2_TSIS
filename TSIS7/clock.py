import pygame 
import time

pygame.init()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My clock")

background = pygame.image.load("blue-clock11.jpg")
minute_hand = pygame.image.load("minutte-removebg-preview1.png")
second_hand = pygame.image.load("secondd-removebg-preview.png")
bottom = pygame.image.load("bottom.png")

background = pygame.transform.scale(background, (WIDTH, HEIGHT))
scale_factor = 0.4
minute_hand = pygame.transform.scale(minute_hand, (int(minute_hand.get_width() * scale_factor), int(minute_hand.get_height() * scale_factor)))
second_hand = pygame.transform.scale(second_hand, (int(second_hand.get_width() * scale_factor), int(second_hand.get_height() * scale_factor)))
bottom = pygame.transform.scale(bottom, (int(bottom.get_width() * scale_factor), int(bottom.get_height() * scale_factor)))

center_x = WIDTH // 2 - 8
center_y = HEIGHT // 2

clock = pygame.time.Clock()
running = True

while running:
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    t = time.localtime()
    minutes = t.tm_min
    seconds = t.tm_sec

    minute_angle = -minutes * 6  
    second_angle = -seconds * 6  

    rotated_minute = pygame.transform.rotate(minute_hand, minute_angle)
    rotated_second = pygame.transform.rotate(second_hand, second_angle)

    minute_rect = rotated_minute.get_rect(center=(center_x, center_y+4))
    second_rect = rotated_second.get_rect(center=(center_x, center_y+4))

    screen.blit(rotated_minute, minute_rect.topleft)
    screen.blit(rotated_second, second_rect.topleft)
    screen.blit(bottom, (center_x - bottom.get_width() // 2 + 20, center_y - bottom.get_height() // 2 ))

   

    pygame.display.flip()
    clock.tick(30)  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()

    