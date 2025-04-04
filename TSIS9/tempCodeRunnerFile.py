def draw_equilateral_triangle(start, end):
    """Создает вершины равностороннего треугольника
    Основание треугольника - горизонтальная линия между start и end
    Высота рассчитывается математически"""
    width = end[0] - start[0]  # Ширина основания
    height = int(abs(width) * math.sqrt(3) / 2)  # Высота равностороннего треугольника
    return [start, end, (start[0] + width//2, start[1] - height)]  # Вершины треугольника