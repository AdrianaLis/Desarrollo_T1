class Equipo:
    def __init__(self,nombre="",partidosganados=0,partidosperdidos=0,setganados=0):
        self.nombre= nombre
        self.partidosganados=partidosganados
        self.partidosperdidos=partidosperdidos
        self.setganados=setganados
    def __str__(self):
        return f" Equipo{self.nombre}"

equipo1 = Equipo("nom1")
equipo2 = Equipo("nom2")

def RegistrarSet(nroequipo):
    if nroequipo==1:
        ganador = equipo1
        rival =equipo2
    else:
        ganador = equipo2  
        rival=equipo1
    ganador.setGanados += 1
    print(f"Set para: {ganador.nombre}")
    print(f"Nombre del equipo: {equipo1.nombre} = Marcador: {equipo1.setganados} - Nombre del equipo {equipo2.nombre} - Marcador{equipo2.setganados}")
    
    if ganador.setganados ==3:
        ganador.partidosganados+=1
        rival.partidosperdidos+=1
        print(f"Ganador del partido es el equipo:{ganador.nombre}")
        equipo1.setganados = 0
        equipo2.setganados = 0
import random
def Puntos(nroequipo):
    if nroequipo==1:
        ganador=equipo1;
    else:
        ganador=equipo2;
    puntos = random.randint(10, 28)

def Puntosextras(nroequipo):
    if nroequipo==1:
        ganador=equipo1;
    else:
        ganador=equipo2;
    puntos = random.randint(0, 6)  
    def JugarPartido():
        print(f"\n--- Iniciando partido: {equipo1.nombre} vs {equipo2.nombre} ---")
    while True:
        
        puntos1 = Puntos() + Puntosextras()
        puntos2 = Puntos() + Puntosextras()
        
        if puntos1 > puntos2:
            termino = RegistrarSet(1)
        else:
            termino = RegistrarSet(2)
            
        if termino: break

while True:
  print("\n--- SISTEMA DE VOLEY ---")
  opc=int(input("1.Ingrese Nombres del equipo -2.Jugar Partido"))
  if opc==1:
        equipo1.nombre = input("Nombre del Equipo 1: ")
        equipo2.nombre = input("Nombre del Equipo 2: ")
        print(f"Rivales listos: {equipo1.nombre} vs {equipo2.nombre}")
      



     
       
        


