#Bucle While

#mostrar los numeros del 1 al 5
#contador = 1
#while contador<=5:
#    print(contador)
#    contador += 1

#obtener promedio de edades de una lista
edades = [13,15,18,12,25]
contador = 0
suma = 0
while contador < len(edades):
    suma = suma + edades[contador]
    contador +=1
print(suma)
promedio = suma / len(edades)
print(promedio)