# Función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

def funcionidentifivocal(vocal):

    a, e, i, o, u = 'a', 'e', 'i', 'o', 'u'

    if vocal == a or vocal == e or vocal == i or vocal == o or vocal == u :
            return True
    else:
        print("No hay vocales")

vocal =str(input('Identificador De Vocales: ',))

print("las vocales", "Son\n", funcionidentifivocal(vocal))