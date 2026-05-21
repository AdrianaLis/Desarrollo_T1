def promedio_recursivo(lista):
    if not lista:
        return 0
    def sumar_elementos(lst_elementos):
        if len(lst_elementos) == 0: 
            return 0
        else: 
            return lst_elementos[0] + sumar_elementos(lst_elementos[1:])

    return sumar_elementos(lista) / len(lista)
    
entrada_usuario = input("Escribe los números que quieras promediar (separados por espacios): ")
mi_lista = [float(x) for x in entrada_usuario.split()]
resultado = promedio_recursivo(mi_lista)

print(f"\nTu lista es: {mi_lista}")
print(f"El promedio es: {resultado}")
