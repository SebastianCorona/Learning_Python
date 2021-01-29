"""Contador de BOB"""


oracion = input('Ingresa la oracción a verificar: ')
oracion = oracion.lower()
contador = 0
print(oracion)
for char in range(len(oracion)):
    if oracion[char: char+3] == 'bob':
        contador = contador + 1


print(contador)