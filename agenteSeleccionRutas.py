import random

ancho_area = 5
alto_area = 5

area = [[random.randint(1, 10) for _ in range(ancho_area)] for _ in range(alto_area)]

inicio = (0, 0)
meta = (alto_area - 1, ancho_area - 1)

direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]

