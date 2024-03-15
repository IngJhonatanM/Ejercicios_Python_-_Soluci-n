#Función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario.
#Escribir la función usando el bucle for anidado.

def superposicion(lista1, lista2):

    for i in lista1:

        for x in lista2:

            if i == x:

                return True

            elif i != x:
                i = False
                x = False
            else:
                return 'Ninguno'
                break 
                  
lista1, lista2 = list(input('Lista1: ', )), list(input('lista2: ', ))

print("El elemento coincidente", "Es\n", superposicion(lista1, lista2))