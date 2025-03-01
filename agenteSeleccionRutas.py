import random

ancho_area = 5
alto_area = 5

area = [[random.randint(1, 10) for _ in range(ancho_area)] for _ in range(alto_area)]

inicio = (0, 0)
meta = (alto_area - 1, ancho_area - 1)

direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def es_movimiento_valido(x, y, explorados):
    return 0 <= x < alto_area and 0 <= y < ancho_area and (x, y) not in explorados

def encontrar_mejor_camino():
    posicion_actual = inicio
    camino = [posicion_actual]
    explorados = set()
    explorados.add(posicion_actual)
    puntos_totales = area[posicion_actual[0]][posicion_actual[1]]
    
    while posicion_actual != meta:
        opciones = []
        for dx, dy in direcciones:
            nuevo_x, nuevo_y = posicion_actual[0] + dx, posicion_actual[1] + dy
            if es_movimiento_valido(nuevo_x, nuevo_y, explorados):
                opciones.append((nuevo_x, nuevo_y))
        
        if not opciones:
            break
        
        mejor_opcion = max(opciones, key=lambda pos: area[pos[0]][pos[1]])
        camino.append(mejor_opcion)
        explorados.add(mejor_opcion)
        puntos_totales += area[mejor_opcion[0]][mejor_opcion[1]]
        posicion_actual = mejor_opcion
    
    return camino, puntos_totales

def mostrar_area():
    for fila in area:
        print(" ".join(f"{v:2}" for v in fila))

print("Área con valores de puntos:")
mostrar_area()
mejor_camino, puntos = encontrar_mejor_camino()
print("\nCamino seleccionado:", mejor_camino)
print("Puntos totales obtenidos:", puntos)