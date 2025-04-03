import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))
base_layer.fill(WHITE) 

current_color = BLACK

# Настройки рисования
LMB_pressed = False  # Флаг нажатия левой кнопки мыши
THICKNESS = 5        # Толщина кисти по умолчанию
current_mode = 'brush'  # Режим рисования по умолчанию - кисть

# Переменные для хранения позиций мыши
start_pos = (0, 0)   # Начальная позиция рисования
current_pos = (0, 0) # Текущая позиция мыши

def calculate_rect(x1, y1, x2, y2):
    """Вычисляет прямоугольник по двум точкам"""
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def draw_preview():
    """Рисует временные очертания фигуры во время перемещения мыши"""
    if current_mode == 'rectangle' and LMB_pressed:
        # Рисуем прямоугольник 
        rect = calculate_rect(*start_pos, *current_pos)
        pygame.draw.rect(screen, current_color, rect, THICKNESS)
    elif current_mode == 'circle' and LMB_pressed:
        # Рисуем круг 
        radius = int(((current_pos[0] - start_pos[0])**2 + (current_pos[1] - start_pos[1])**2)**0.5)
        pygame.draw.circle(screen, current_color, start_pos, radius, THICKNESS)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        # Событие закрытия окна
        if event.type == pygame.QUIT:
            running = False
        
        # Обработка нажатия левой кнопки мыши
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMB_pressed = True  
            start_pos = event.pos  
            current_pos = event.pos
            # Если режим кисти - рисуем начальную точку
            if current_mode == 'brush':
                pygame.draw.circle(base_layer, current_color, start_pos, THICKNESS//2)
        
        # Обработка движения мыши
        if event.type == pygame.MOUSEMOTION:
            current_pos = event.pos  # Обновляем текущую позицию
            if LMB_pressed:
                # В режиме кисти рисуем линию
                if current_mode == 'brush':
                    pygame.draw.line(base_layer, current_color, start_pos, current_pos, THICKNESS)
                    start_pos = current_pos  
                # В режиме ластика рисуем белые круги
                elif current_mode == 'eraser':
                    pygame.draw.circle(base_layer, WHITE, current_pos, THICKNESS)
        
        # Обработка отпускания кнопки мыши
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if LMB_pressed:
                # Если режим прямоугольника - рисуем прямоугольник
                if current_mode == 'rectangle':
                    rect = calculate_rect(*start_pos, *current_pos)
                    pygame.draw.rect(base_layer, current_color, rect, THICKNESS)
                # Если режим круга - рисуем круг
                elif current_mode == 'circle':
                    radius = int(((current_pos[0] - start_pos[0])**2 + (current_pos[1] - start_pos[1])**2)**0.5)
                    pygame.draw.circle(base_layer, current_color, start_pos, radius, THICKNESS)
            LMB_pressed = False  
        
        # Обработка нажатий клавиш
        if event.type == pygame.KEYDOWN:
            # Увеличение толщины
            if event.key == pygame.K_EQUALS:
                THICKNESS += 1
            # Уменьшение толщины 
            elif event.key == pygame.K_MINUS:
                THICKNESS = max(1, THICKNESS - 1)
            # Изменение цвета
            elif event.key == pygame.K_1:
                current_color = BLACK  
            elif event.key == pygame.K_2:
                current_color = RED    
            elif event.key == pygame.K_3:
                current_color = BLUE   
            # Изменение режима рисования
            elif event.key == pygame.K_r:
                current_mode = 'rectangle'  
            elif event.key == pygame.K_b:
                current_mode = 'brush'      
            elif event.key == pygame.K_c:
                current_mode = 'circle'    
            elif event.key == pygame.K_e:
                current_mode = 'eraser'     
    
    # Отрисовка базового слоя
    screen.blit(base_layer, (0, 0))
    # Рисуем временные очертания фигур
    draw_preview()
    
    # Отображение информации о текущем режиме
    font = pygame.font.SysFont(None, 24)
    mode_text = font.render(
        f"Mode: {current_mode} | Thickness: {THICKNESS} (+/-)", 
        True, BLACK)
    screen.blit(mode_text, (10, 10))
    
    # Обновление экрана
    pygame.display.flip()
    # Ограничение частоты кадров (60 FPS)
    clock.tick(60)

pygame.quit()