# Construir un pequeño programa que convierta números binarios en enteros. 

numeros_bi = input("Ingrese un numero binario: ")

def convertidor(numeros_bi):
  numeros_bi = str(numeros_bi)
  decimal = 0
  exp = len (numeros_bi) -1
  for i in numeros_bi:
    decimal += (int(i) * 2**(exp))
    exp = exp - 1
    return decimal

print("los numeros ahora Son Enteros\n", convertidor(numeros_bi))