def funcion_recursiva(numero):
     numero-=1;
     if numero >0:
           print(numero)
           funcion_recursiva(numero)
     else:
           print('Holaaaa')
   


numero_usuario = int(input("Ingresa un número: "));
funcion_recursiva(numero_usuario)