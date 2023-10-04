resultado = 0

def suma(a,b):
    global resultado
    resultado = a + b
    return resultado

suma(7,3)
print(resultado)