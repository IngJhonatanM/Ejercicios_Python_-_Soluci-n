# Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga. 


def encontrar_palabra_mas_larga(lista_palabras):
  """
  Esta función toma una lista de palabras y devuelve la palabra más larga.

  Parámetros:
    lista_palabras: una lista de strings.

  Retorno:
    la palabra más larga en la lista.
  """

  palabra_mas_larga = ""
  for palabra in lista_palabras:
    if len(palabra) > len(palabra_mas_larga):
      palabra_mas_larga = palabra

  return palabra_mas_larga

# Ejemplo de uso
lista_palabras = ["Hola", "mundo", "esta", "es", "una", "lista", "de", "Amoxicilina"]
palabra_mas_larga = encontrar_palabra_mas_larga(lista_palabras)
print(f"La palabra más larga es: {palabra_mas_larga}")