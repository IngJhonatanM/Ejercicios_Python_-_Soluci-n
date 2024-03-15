#Función Para Calcular La longitud de una lista oh String


def largo_cadena (lista):
    cont = 0
    for i in lista:
        cont += 1
    return cont

lista =input('Elemento: ',)

print("la longitud", "Es\n", largo_cadena(lista))
