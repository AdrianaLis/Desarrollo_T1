def buscar_mayor_recursivo(lista):
    if len(lista) == 1:
        return lista[0]
    mayor_del_resto = buscar_mayor_recursivo(lista[1:]) 
    if lista[0] > mayor_del_resto:
        return lista[0]
    else:
        return mayor_del_resto

entrada = input("Ingresa varios números separados por espacios: ")
mi_lista = [int(x) for x in entrada.split()]
resultado = buscar_mayor_recursivo(mi_lista)
print("El mayor valor de tu lista es:", resultado)