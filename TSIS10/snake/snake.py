import pygame
import random
import psycopg2

from config_snake import host, database, password, user

conn = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = database
    )

cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR UNIQUE NOT NULL,
    level INT DEFAULT 1,
    score INT DEFAULT 0
);
""")
cur.execute("""
CREATE TABLE IF NOT EXISTS user_score (
    score_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    level INT,
    score INT
);
""")

# --- Настройки --- 
WIDTH, HEIGHT = 600, 600
CELL = 30
FPS = 5

# --- Цвета --- 
WHITE, GRAY, BLACK = (255,255,255), (200,200,200), (0,0,0)
RED, GREEN, YELLOW, BLUE = (255,0,0), (0,255,0), (255,255,0), (0,100,255)

# --- Окно --- 
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# --- Игрок --- 
username = input("Enter your username: ")

def draw_grid():
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            color = WHITE if (i + j) % 2 == 0 else GRAY
            pygame.draw.rect(screen, color, (j * CELL, i * CELL, CELL, CELL))

def get_or_create_user(username):
    cur.execute("SELECT user_id, level, score FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    if user:
        user_id, level, score = user
        print(f"Welcome back, {username}! Your previous level: {level}, score: {score}")
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING user_id", (username,))
        user_id = cur.fetchone()[0]
        cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)", (user_id, 0, 1))
        conn.commit()
        print(f"Welcome, {username}! Starting a new game.")
    return user_id

user_id = get_or_create_user(username)

# --- Игровой процесс ---
def update_user_level(user_id, level):
    cur.execute("UPDATE users SET level = %s WHERE user_id = %s", (level, user_id))
    conn.commit()

class Point:
    def __init__(self, x, y): self.x, self.y = x, y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx, self.dy = 1, 0
        self.score = 0
        self.level = 1
        self.food_count = 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        self.body[0].x += self.dx
        self.body[0].y += self.dy
        self.body[0].x %= WIDTH // CELL
        self.body[0].y %= HEIGHT // CELL

    def draw(self):
        pygame.draw.rect(screen, RED, (self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL))
        for seg in self.body[1:]:
            pygame.draw.rect(screen, YELLOW, (seg.x * CELL, seg.y * CELL, CELL, CELL))

    def check_self_collision(self):
        head = self.body[0]
        return any(head.x == s.x and head.y == s.y for s in self.body[1:])

    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.body.append(Point(head.x, head.y))
            food.rand_pos()
            self.score += random.randint(5, 15)
            self.food_count += 1
            if self.food_count % 3 == 0:
                self.level += 1
                wall.load_level(self.level)
                global FPS
                FPS += 1
                update_user_level(user_id, self.level)
            return True
        return False

class Wall:
    def __init__(self): self.body = []
    def load_level(self, level):
        self.body.clear()
        if level == 2:
            self.body += [Point(i, 10) for i in range(5, 15)]
        elif level == 3:
            self.body += [Point(10, i) for i in range(5, 15)]
        elif level == 4:
            self.body += [Point(i, i) for i in range(7, 12)]
        elif level == 5:
            self.body += [Point(i, 20 - i) for i in range(7, 12)]
        elif level == 6:
            self.body += [Point(7, i) for i in range(7, 17)] + [Point(i, 7) for i in range(7, 17)]
        elif level == 7:
            for i in range(5, 15):
                if i % 2 == 0:
                    self.body.append(Point(i, 5))
                    self.body.append(Point(i, 15))
    def draw(self):
        for wall in self.body:
            pygame.draw.rect(screen, BLUE, (wall.x * CELL, wall.y * CELL, CELL, CELL))
    def check_collision(self, head):
        return any(head.x == w.x and head.y == w.y for w in self.body)

class Food:
    def __init__(self): self.pos = Point(0, 0); self.rand_pos()
    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))
    def rand_pos(self):
        while True:
            new_pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))
            if not any(seg.x == new_pos.x and seg.y == new_pos.y for seg in snake.body) and \
               not any(w.x == new_pos.x and w.y == new_pos.y for w in wall.body):
                self.pos = new_pos
                break

snake = Snake()
wall = Wall()
wall.load_level(snake.level)
food = Food()
running = True

while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx, snake.dy = 1, 0
            elif event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx, snake.dy = -1, 0
            elif event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dx, snake.dy = 0, 1
            elif event.key == pygame.K_UP and snake.dy == 0:
                snake.dx, snake.dy = 0, -1
            elif event.key == pygame.K_p:
                print("Game paused. Saving...")
                cur.execute("UPDATE users SET level = %s, score = %s WHERE user_id = %s", (snake.level, snake.score, user_id))
                cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)", (user_id, snake.score, snake.level))
                conn.commit()
                paused = True
                while paused:
                    for pe in pygame.event.get():
                        if pe.type == pygame.KEYDOWN and pe.key == pygame.K_p:
                            paused = False

    draw_grid()
    snake.move()
    if snake.check_self_collision() or wall.check_collision(snake.body[0]):
        font = pygame.font.SysFont(None, 100)
        text = font.render("Game Over!", True, RED)
        screen.blit(text, (WIDTH // 5, HEIGHT // 3))
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False
        continue

    snake.check_collision(food)
    snake.draw()
    food.draw()
    wall.draw()

    font = pygame.font.Font(None, 36)
    info = font.render(f"Score: {snake.score}  Level: {snake.level}", True, BLACK)
    screen.blit(info, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

cur.execute("UPDATE users SET level = %s, score = %s WHERE user_id = %s", (snake.level, snake.score, user_id))
cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)", (user_id, snake.score, snake.level))
conn.commit()
cur.close()
conn.close()
pygame.quit()