import random

#la matrz que sea de 5 * 5 que es mi cuadricula
ancho = 5
alto = 5



mapa = [[0 for _ in range(ancho)] for _ in range(alto)]


posicion = [0, 0]


visitados = [[False for _ in range(ancho)] for _ in range(alto)]
visitados[posicion[0]][posicion[1]] = True

movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def es_movimiento_valido(x, y):
    return 0 <= x < alto and 0 <= y < ancho and mapa[x][y] == 0 and not visitados[x][y]

def mover_explorador():
    x, y = posicion
    opciones = []
    
    for dx, dy in movimientos:
        nuevo_x, nuevo_y = x + dx, y + dy
        if es_movimiento_valido(nuevo_x, nuevo_y):
            opciones.append((nuevo_x, nuevo_y))
    
    if opciones:
        nuevo_x, nuevo_y = random.choice(opciones)
        posicion[0], posicion[1] = nuevo_x, nuevo_y
        visitados[nuevo_x][nuevo_y] = True
        print(f"Explorador se movió a: ({nuevo_x}, {nuevo_y})")
    else:
        print("No hay más caminos nuevos por explorar.")
        
def mostrar_mapa():
    for i in range(alto):
        for j in range(ancho):
            if [i, j] == posicion:
                print("E", end=" ") 
            elif visitados[i][j]:
                print("V", end=" ")  
            elif mapa[i][j] == 1:
                print("X", end=" ")  
            else:
                print("*", end=" ")  
        print()


print("Mapa inicial:")
mostrar_mapa()

for _ in range(25):  
    mover_explorador()
    mostrar_mapa()
