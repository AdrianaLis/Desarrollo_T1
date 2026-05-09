pesos = [10, 20, 30]
valores = [60, 100, 120]
nombres = ["Caja 1", "Caja 2", "Caja 3"]

m = float(input("Peso máximo de la mochila: "))
tabla = []
for i in range(len(pesos)):
    rentabilidad = valores[i] / pesos[i]
    tabla.append([rentabilidad, pesos[i], valores[i], nombres[i]])
tabla.sort(reverse=True)
peso_actual = 0
soles_totales = 0
print("\n--- Selección ---")

for rentabilidad, peso, valor, nombre in tabla:
    if peso_actual + peso <= m:
        peso_actual += peso
        soles_totales += valor
        print(f"Llevo {nombre} completa")
    else:
        sobrante = m - peso_actual
        if sobrante > 0:
            pago_parcial = sobrante * rentabilidad
            soles_totales += pago_parcial
            peso_actual += sobrante
            print(f"Llevo un pedazo de {nombre} (peso: {sobrante})")
        break

print(f"\nSoles totales: S/{soles_totales}")
print(f"Peso total: {peso_actual}kg")
