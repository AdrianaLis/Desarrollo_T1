def mostrar_multiplos_tres(numero):
    if numero < 1:
        return
    mostrar_multiplos_tres(numero - 1)
    if numero % 3 == 0:
        print(numero)

numero_usuario = int(input("Ingresa un número: "));
mostrar_multiplos_tres(numero_usuario)
