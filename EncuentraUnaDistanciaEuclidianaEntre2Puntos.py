# 1.- Definir una funcion max() que tome como argumentos 2 numeros y devuelva El mayor de ellos

punto_a = (2,3)
punto_b = (10,8)

def Distance_Euclidiana(puntoa, puntob):
    
    diferencias = [puntoa[x] - puntob[x] for x in range(len(puntoa))]
    diferencias_agrupadas = [diferencias ** 2 for diferencias in diferencias]
    sum_of_squares = sum(diferencias_agrupadas)
    return sum_of_squares ** 0.5

print(Distance_Euclidiana(punto_a, punto_b))