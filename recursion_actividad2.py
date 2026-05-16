def sumar_multiplos_cinco(lista):
  
    if len(lista) == 0:
        return 0
    suma_del_resto = sumar_multiplos_cinco(lista[1:])
    if lista[0] % 5 == 0: 
        return lista[0] + suma_del_resto
    else:    
        return suma_del_resto

entrada = input("Ingresa varios números separados por espacios: ")
mi_lista = [int(x) for x in entrada.split()]
resultado = sumar_multiplos_cinco(mi_lista)
print("La suma de los múltiplos de 5 es:", resultado)