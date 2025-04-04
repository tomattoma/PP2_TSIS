import pygame  
import math    

pygame.init()

BLACK = (0, 0, 0)      
WHITE = (255, 255, 255)
RED = (255, 0, 0)       
BLUE = (0, 0, 255)    

WIDTH, HEIGHT = 800, 600  
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
base_layer = pygame.Surface((WIDTH, HEIGHT))  
base_layer.fill(WHITE)  

current_color = BLACK    # Текущий цвет рисования
LMB_pressed = False      # Флаг нажатия левой кнопки мыши 
THICKNESS = 5            # Толщина линий по умолчанию
current_mode = 'brush'   # Текущий режим рисования (по умолчанию - кисть)
start_pos = (0, 0)       # Начальная точка рисования
current_pos = (0, 0)     # Текущая позиция курсора

# ---- ФУНКЦИИ ДЛЯ РИСОВАНИЯ ФИГУР ----

def calculate_rect(x1, y1, x2, y2):
    """Вычисляет координаты прямоугольника по двум диагональным точкам
    Возвращает объект pygame.Rect c правильными координатами"""
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def draw_right_triangle(start, end):
    """Создает вершины прямоугольного треугольника c прямым углом в стартовой точке
    Возвращает список из трех точек (кортежей)"""
    return [start, (start[0], end[1]), end]

def draw_equilateral_triangle(start, end):
    """Создает вершины равностороннего треугольника
    Основание треугольника - горизонтальная линия между start и end
    Высота рассчитывается математически"""
    
    x1, y1 = start
    x2, y2 = end
    
    # Учитываем направление рисования
    if x1 > x2:
        x1, x2 = x2, x1  # Меняем местами, если пользователь рисует влево
    
    # Вычисляем ширину и высоту треугольника
    width = x2 - x1
    height = int(width * math.sqrt(3) / 2)  # Формула для высоты равностороннего треугольника
    
    # Координаты трех вершин
    point1 = (x1, y1)  # Левая нижняя вершина
    point2 = (x2, y1)  # Правая нижняя вершина
    point3 = (x1 + width // 2, y1 - height)  # Верхняя вершина (над основанием)
    
    return [point1, point2, point3]


def draw_rhombus(start, end):
    """Создает вершины ромба
    Точки start и end задают диагонали ромба
    Возвращает список из четырех точек"""
    center_x = (start[0] + end[0]) // 2  # Центр по X
    center_y = (start[1] + end[1]) // 2  # Центр по Y
    return [
        (center_x, start[1]),  # Верхняя точка
        (end[0], center_y),     # Правая точка
        (center_x, end[1]),     # Нижняя точка
        (start[0], center_y)    # Левая точка
    ]

def draw_preview():
    """Функция для отображения предварительного просмотра фигуры"""
    if LMB_pressed:  # Если кнопка мыши нажата
        if current_mode == 'rectangle':  # Режим прямоугольника
            rect = calculate_rect(*start_pos, *current_pos)
            pygame.draw.rect(screen, current_color, rect, THICKNESS)
        elif current_mode == 'circle':  # Режим круга
            radius = int(math.hypot(current_pos[0]-start_pos[0], current_pos[1]-start_pos[1]))
            pygame.draw.circle(screen, current_color, start_pos, radius, THICKNESS)
        elif current_mode == 'square':  # Режим квадрата
            size = min(abs(current_pos[0]-start_pos[0]), abs(current_pos[1]-start_pos[1]))
            rect = pygame.Rect(start_pos[0], start_pos[1], size, size)
            pygame.draw.rect(screen, current_color, rect, THICKNESS)
        elif current_mode == 'right_triangle':  # Прямоугольный треугольник
            points = draw_right_triangle(start_pos, current_pos)
            pygame.draw.polygon(screen, current_color, points, THICKNESS)
        elif current_mode == 'equilateral_triangle':  # Равносторонний треугольник
            points = draw_equilateral_triangle(start_pos, current_pos)
            pygame.draw.polygon(screen, current_color, points, THICKNESS)
        elif current_mode == 'rhombus':  # Ромб
            points = draw_rhombus(start_pos, current_pos)
            pygame.draw.polygon(screen, current_color, points, THICKNESS)

running = True  
clock = pygame.time.Clock() 

while running:
    for event in pygame.event.get():
        # Событие закрытия окна
        if event.type == pygame.QUIT:
            running = False
        
        # Событие нажатия левой кнопки мыши
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMB_pressed = True
            start_pos = event.pos  # Запоминаем начальную позицию
            current_pos = event.pos
            # Если режим кисти - рисуем начальную точку
            if current_mode == 'brush':
                pygame.draw.circle(base_layer, current_color, start_pos, THICKNESS//2)
        
        # Событие движения мыши
        if event.type == pygame.MOUSEMOTION:
            current_pos = event.pos  # Обновляем текущую позицию
            if LMB_pressed:  
                if current_mode == 'brush':  # Режим кисти
                    pygame.draw.line(base_layer, current_color, start_pos, current_pos, THICKNESS)
                    start_pos = current_pos  # Обновляем начальную позицию для плавного рисования
                elif current_mode == 'eraser':  # Режим ластика
                    pygame.draw.circle(base_layer, WHITE, current_pos, THICKNESS)
        
        # Событие отпускания кнопки мыши
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if LMB_pressed: 
                # Рисуем фигуру на базовом слое в зависимости от режима
                if current_mode == 'rectangle':
                    rect = calculate_rect(*start_pos, *current_pos)
                    pygame.draw.rect(base_layer, current_color, rect, THICKNESS)
                elif current_mode == 'circle':
                    radius = int(math.hypot(current_pos[0]-start_pos[0], current_pos[1]-start_pos[1]))
                    pygame.draw.circle(base_layer, current_color, start_pos, radius, THICKNESS)
                elif current_mode == 'square':
                    size = min(abs(current_pos[0]-start_pos[0]), abs(current_pos[1]-start_pos[1]))
                    rect = pygame.Rect(start_pos[0], start_pos[1], size, size)
                    pygame.draw.rect(base_layer, current_color, rect, THICKNESS)
                elif current_mode == 'right_triangle':
                    points = draw_right_triangle(start_pos, current_pos)
                    pygame.draw.polygon(base_layer, current_color, points, THICKNESS)
                elif current_mode == 'equilateral_triangle':
                    points = draw_equilateral_triangle(start_pos, current_pos)
                    pygame.draw.polygon(base_layer, current_color, points, THICKNESS)
                elif current_mode == 'rhombus':
                    points = draw_rhombus(start_pos, current_pos)
                    pygame.draw.polygon(base_layer, current_color, points, THICKNESS)
            LMB_pressed = False  
        
        # Обработка нажатий клавиш
        if event.type == pygame.KEYDOWN:
            # Изменение толщины
            if event.key == pygame.K_EQUALS:  
                THICKNESS += 1
            elif event.key == pygame.K_MINUS:  
                THICKNESS = max(1, THICKNESS - 1) 
            
            # Изменение цвета
            elif event.key == pygame.K_1:  # Цифра 1
                current_color = BLACK
            elif event.key == pygame.K_2:  # Цифра 2
                current_color = RED
            elif event.key == pygame.K_3:  # Цифра 3
                current_color = BLUE
            
            # Изменение режима рисования
            elif event.key == pygame.K_r:  
                current_mode = 'rectangle'  # Прямоугольник
            elif event.key == pygame.K_b:  
                current_mode = 'brush'     # Кисть
            elif event.key == pygame.K_c:  
                current_mode = 'circle'    # Круг
            elif event.key == pygame.K_e: 
                current_mode = 'eraser'    # Ластик
            elif event.key == pygame.K_s:
                current_mode = 'square'    # Квадрат
            elif event.key == pygame.K_t:  
                current_mode = 'right_triangle'  # Прямоугольный треугольник
            elif event.key == pygame.K_q: 
                current_mode = 'equilateral_triangle'  # Равносторонний треугольник
            elif event.key == pygame.K_h:  
                current_mode = 'rhombus'  # Ромб
    
    # Отрисовка
    screen.blit(base_layer, (0, 0))  # Отображаем базовый слой
    draw_preview()  
    pygame.display.flip()  # Обновляем экран
    clock.tick(60)  # Ограничение до 60 FPS

pygame.quit()