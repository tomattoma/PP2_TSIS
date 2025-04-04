import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

#Настройка FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Создание цветов
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (139, 128, 0)

#Другие переменные для использования в программе
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
SCORE_COINS = 0

#Настройка шрифтов
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
special_coin_image = pygame.image.load("bag-removebg-preview.png")
special_coin_image = pygame.transform.scale(special_coin_image, (80, 80))
background = pygame.image.load("AnimatedStreet.png")

#Создание белого экрана 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), SCREEN_HEIGHT) 

    def move(self):
        self.rect.y += 5 
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Special_Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = special_coin_image
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), SCREEN_HEIGHT) 

    def move(self):
        self.rect.y += 5 
        if self.rect.top > SCREEN_HEIGHT and SCORE % 10 == 0:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


                   
#Настройка спрайтов        
P1 = Player()
E1 = Enemy()
C1 = Coins()
S1 = Special_Coin()

#Создание групп спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
special_coin = pygame.sprite.Group()
special_coin.add(S1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
all_sprites.add(S1)

#Добавление нового пользовательского события 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(-1)

#Игровой цикл
while True:
    #Обрабатываем все события, происходящие в игре  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render("Round: "+str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))


    #Перемещение и перерисовка всех спрайтов
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    
    if pygame.sprite.spritecollideany(P1, coins):
        pygame.mixer.Sound('coinget.wav').play()
        SCORE_COINS += 1
        for coin in coins:
            coin.kill()  # Удаляем собранную монету
            new_coin = Coins()  # Создаём новую монету
            coins.add(new_coin)
            all_sprites.add(new_coin)
    
    if pygame.sprite.spritecollideany(P1, special_coin):
        pygame.mixer.Sound('coinget.wav').play()
        SCORE_COINS += 10
        for s_coin in special_coin:
            s_coin.kill()  # Удаляем собранную монету
            new_coin = Special_Coin()  # Создаём новую монету
            special_coin.add(new_coin)
            all_sprites.add(new_coin)
    
    scores_coins = font_small.render("Coins: "+str(SCORE_COINS), True, YELLOW)
    DISPLAYSURF.blit(scores_coins, (9,30))   

    #Проверка столкновения игрока с врагом
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(0.5)
                    
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
         
    pygame.display.update()
    FramePerSec.tick(FPS)
