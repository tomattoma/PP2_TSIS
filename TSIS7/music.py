import pygame
import os


pygame.init()
pygame.mixer.init()


muzon_dir = "music"
tracks = [os.path.join(muzon_dir, f) for f in os.listdir(muzon_dir) if f.endswith('.mp3')]

if not tracks:
    print("There are no audio files")
    exit()

print("Found tracks:", tracks)  

current_track = 0
paused = False 


WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")


WHITE = (224, 255, 255)
BLACK = (0, 0, 0)
BLUE = (255, 182, 193)


font = pygame.font.SysFont("ATC Citrine", 28)


def draw_text(text, x, y):
    text_surface = font.render(text, True, BLACK)
    screen.blit(text_surface, (x, y))

def play_music():
    global paused
    pygame.mixer.music.load(tracks[current_track])
    pygame.mixer.music.play()
    paused = False  # Когда начинается новый трек он же не в паузе вооо
    print(f"Now playing: {tracks[current_track]}")


def stop_music():
    global paused
    pygame.mixer.music.stop()
    paused = False  # Музыка остановлена птмшт паузы нет
    print("Music stopped")


def next_track():
    global current_track
    current_track = (current_track + 1) % len(tracks)
    play_music()


def previous_track():
    global current_track
    current_track = (current_track - 1) % len(tracks)
    play_music()

# Кнопкалардын турган жеры 
buttons = {
    "Play | ❚❚": pygame.Rect(108, 200, 100, 40),
    " Stop": pygame.Rect(219, 200, 78, 40),
    "Next": pygame.Rect(308, 200, 70, 40),
    "Previous": pygame.Rect(108, 250, 100, 40),
    "Quit": pygame.Rect(308, 250, 70, 40)
}



running = True
while running:
    screen.fill(WHITE)

    # Отображаем текущий трек
    track_name = os.path.basename(tracks[current_track])
    draw_text(f"Now playing: {track_name}", 95, 90)

   
    for text, rect in buttons.items():
        pygame.draw.rect(screen, BLUE, rect)
        draw_text(text, rect.x + 10, rect.y + 10)

    pygame.display.flip()  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                    print("Resuming track")
                else:
                    pygame.mixer.music.pause()
                    paused = True
                    print("Track paused")

            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_p:
                previous_track()
            elif event.key == pygame.K_q:
                running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for text, rect in buttons.items():
                if rect.collidepoint(mouse_pos):
                    if text == "Play | ❚❚":
                        if paused:
                            pygame.mixer.music.unpause()
                            paused = False
                            print("Resuming track")
                        else:
                            pygame.mixer.music.pause()
                            paused = True
                            print("Track paused")
                    elif text == " Stop":
                        stop_music()
                    elif text == "Next":
                        next_track()
                    elif text == "Previous":
                        previous_track()
                    elif text == "Quit":
                        running = False

pygame.quit()
