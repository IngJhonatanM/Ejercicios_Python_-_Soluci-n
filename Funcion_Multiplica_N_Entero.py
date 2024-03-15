# Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n.
#  Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

n_numero  = int(input('Número: ', ))

def generar_n_caracteres(n_numero, x ):
    total = n_numero * x 
    return total

print("El resultado de caracteres", "Es\n", generar_n_caracteres(n_numero, x ))
    
        
    