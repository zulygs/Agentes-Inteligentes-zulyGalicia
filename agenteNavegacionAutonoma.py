from collections import deque 

# asi hacemos  la matriz de 5*5
laberinto = [
    ['A', 'O', 'X', 'O', 'X'], 
    ['O', 'O', 'X', 'O', 'X'],   
    ['O', 'O', 'O', 'O', 'X'],  
    ['X', 'X', 'X', 'O', 'X'], 
    ['O', 'O', 'O', 'O', 'Meta']    
]

filas = 5
columnas = 5

posicion_inicial = (0, 0)

posicion_meta = (4, 4)

movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def es_movimiento_valido(fila, columna):
    return 0 <= fila < filas and 0 <= columna < columnas and laberinto[fila][columna] != 'X'

def buscar_ruta(posicion_inicial, posicion_meta):
 
    cola = deque()
    cola.append((posicion_inicial, [posicion_inicial]))  
    celdas_visitadas = set()  
    celdas_visitadas.add(posicion_inicial)

    while cola:
        (fila_actual, columna_actual), camino = cola.popleft() 

        if (fila_actual, columna_actual) == posicion_meta:
            return camino


        for movimiento_fila, movimiento_columna in movimientos:
            nueva_fila = fila_actual + movimiento_fila
            nueva_columna = columna_actual + movimiento_columna
            if es_movimiento_valido(nueva_fila, nueva_columna) and (nueva_fila, nueva_columna) not in celdas_visitadas:
                celdas_visitadas.add((nueva_fila, nueva_columna))  
                cola.append(((nueva_fila, nueva_columna), camino + [(nueva_fila, nueva_columna)])) 

    return None  

def mostrar_laberinto_con_ruta(camino):
    for fila in range(filas):
        for columna in range(columnas):
            if (fila, columna) in camino:
                print("A", end=" ")  
            else:
                print(laberinto[fila][columna], end=" ")  
        print()

ruta = buscar_ruta(posicion_inicial, posicion_meta)

if ruta:
    print("Ruta encontrada:")
    mostrar_laberinto_con_ruta(ruta)
else:
    print("No se encontró una ruta válida.")