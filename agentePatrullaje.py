import random
import time

class agente_Patrullaje_Reflejo:
    def __init__(self, recorrido):
        self.recorrido = recorrido
        self.punto_actual = 0
        self.sentido = 1
    
    def hay_obstaculo(self):
        return random.random() < 0.2
    
    def cambiar_sentido(self):
        nuevo_sentido = random.choice([-1, 1])
        if nuevo_sentido == self.sentido:
            nuevo_sentido *= -1
        self.sentido = nuevo_sentido
        print("Obstáculo encontrado! Cambiando dirección a:", "Derecha" if self.sentido == 1 else "Izquierda")
    
    def avanzar(self):
        if self.hay_obstaculo():
            self.cambiar_sentido()
        
        nuevo_punto = self.punto_actual + self.sentido
        if 0 <= nuevo_punto < len(self.recorrido):
            self.punto_actual = nuevo_punto
        else:
            self.sentido *= -1
        
        print(f"Patrullero en: {self.recorrido[self.punto_actual]}")

recorrido = ["Ruta 1", "Ruta 2", "Ruta 3", "Ruta 4", "Ruta 5"]
patrullero = agente_Patrullaje_Reflejo(recorrido)

movimientos_totales = 20
for _ in range(movimientos_totales):
    patrullero.avanzar()
    time.sleep(1)