from abc import ABC, abstractmethod

class Transporte(ABC): #Principio de Abstraccion
    def __init__(self, capacidad):
        self._capacidad = capacidad #Atributo Privado

    @abstractmethod
    def mover(self): #Atributo privado
        pass
#Inicio Herencia
class Colectivo(Transporte):
    def mover(self):
        print(f"El colectivo se mueve por la ciudad con {self._capacidad} pasajeros.")

class Tren(Transporte):
    def mover(self):
        print(f"El tren recorre largas distancias con {self._capacidad} pasajeros.")

class Avion(Transporte):
    def mover(self):
        print(f"El avión vuela a gran altitud con {self._capacidad} pasajeros.")
#Fin Herencia

def iniciar_viaje(lista_transportes):
    for transporte in lista_transportes:
        transporte.mover()

if __name__ == "__main__":
    #Polimorfismo
    colectivo = Colectivo(50)
    tren = Tren(300)
    avion = Avion(180)
    #Fin Poliformismo

    medios = [colectivo, tren, avion]
    iniciar_viaje(medios)