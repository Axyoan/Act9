from particula import Particula

class AdministradorParticula:
    def __init__(self):
        self.__particulas = []

    def agregar_inicio(self, particula:Particula):
        self.__particulas.append(particula)

    def agregar_final(self, particula:Particula):
        self.__particulas.insert(0, particula)

    def mostrar(self):
        for p in self.__particulas:
            print(p, '\n')

p01  = Particula(ID=1, origen_x=0, origen_y=0, destino_x=5, destino_y=10, velocidad=3)
p02 = Particula(2, 2, 3, -2, 4, 25, 100, 150, 150)
administrador = AdministradorParticula()
administrador.agregar_final(p01)
administrador.agregar_inicio(p02)
administrador.agregar_inicio(p01)
administrador.mostrar()
