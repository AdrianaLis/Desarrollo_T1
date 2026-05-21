def invertir_cadena(texto):
   if len(texto) <= 1:
        return texto
   return invertir_cadena(texto[1:]) + texto[0]
   
texto_usuario = input("Ingresa una cadena de texto: ")
resultado = invertir_cadena(texto_usuario)

print(f"Texto invertido: {resultado}")