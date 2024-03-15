# 1.- Definir una funcion max() que tome como argumentos 2 numeros y devuelva El mayor de ellos

def max (n1, n2):

    if n1 > n2:
        return n1

    elif n2 > n1:

            return n2
    else:
        return (max(n1, n2))


n1, n2, = int(input('Número1: ', )), int(input('Número2: ', ))

print("El número mayor", "es\n", max(n1,n2))
