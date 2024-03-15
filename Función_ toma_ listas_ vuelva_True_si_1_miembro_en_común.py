# Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común
# o devuelva False de lo contrario.
# Escribir la función usando el bucle for anidado.

lista1  = list(input('Lista#1: ', ))
lista2  = list(input('Lista#2: ', ))

def superposicion (lista1, lista2):
    
    for i in lista1:
        for x in lista2:
            if i == x:
                return True
            
        return False

print("El resultado", "Es\n", superposicion(lista1, lista2))