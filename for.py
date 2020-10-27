"""Clase de For"""


names = ['Abraham', 'César', 'Daniel', 'Daniela', 'Diego', 'Edgar']

for name in names:
    print(f'Student: {name}')
else: 
    print('No hay más nombres')

string = 'Sebastián'

for char in string:
    print (char)

for char in string:
    if char != 'a':
        print(char)
else:
    print ('Fuera del for')

numbers = []

for number in range(0, 21, 2):
    numbers.append(number)

print (numbers)