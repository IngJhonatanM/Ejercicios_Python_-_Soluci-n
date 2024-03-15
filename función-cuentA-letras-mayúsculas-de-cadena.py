def contar_letras_mayusculas(cadena):
  """
  Esta función cuenta la cantidad de letras mayúsculas en una cadena.

  Parámetros:
    cadena: una cadena de caracteres.

  Retorno:
    la cantidad de letras mayúsculas en la cadena.
  """

  contador_mayusculas = 0
  for letra in cadena:
    if letra.isupper():
      contador_mayusculas += 1

  return contador_mayusculas

# Ejemplo de uso
cadena = input("Ingrese una cadena: ")
numero_mayusculas = contar_letras_mayusculas(cadena)
print(f"La cadena tiene {numero_mayusculas} letras mayúsculas.")
