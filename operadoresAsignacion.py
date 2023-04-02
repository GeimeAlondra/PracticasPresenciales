print('Practica de operadores de asignacion')

nombre = 'Hola'

#print(nombre)

nombre += input('Escribe tu nombre: ')
nombre = nombre + input('Escribe tu apellido: ')
print(nombre, ', esto es el incremento y descrementos de variables \n')

print('Incremento o aumento: ')
x = 1

print('El valor inicial de x es: ', x)

x += 1
x += 1 
x += 3
x += 2

print('El valor final de x es: ', x, '\n')

print('Decremento o disminucion: ')
print('El valor inicial de x es: ', x)

x -= 1
x -= 1 
x -= 1

print('El valor final de la variable x es: ', x)

print('Otras asignaciones con operadores diferentes')

x *= 3

print(x)

x /= 2

print(x)

x %= 5

print(x)