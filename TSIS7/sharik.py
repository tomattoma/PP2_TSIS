import pygame

pygame.init()
screen=pygame.display.set_mode((400,300))
pygame.display.set_caption("Moving Ball")
done=False

ball_radius=25
x=30
y=30
speed=20

clock=pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y-ball_radius-speed>=0:y-=20
    if pressed[pygame.K_DOWN] and y+ball_radius+speed<=300: y+=20
    if pressed[pygame.K_LEFT] and x-ball_radius-speed>=0: x-=20
    if pressed[pygame.K_RIGHT] and x+ball_radius+speed<=400: x+=20

    screen.fill((255,255,255))
    pygame.draw.circle(screen, (255,0,0), (x,y), ball_radius)

    pygame.display.flip()
    clock.tick(60)