# Ejemplo 1

print('Comienzo de bucle For')

for i in [0,1,2]:
    print('Hola')
    
print('\nFin')

# Ejemplo 2

print('Comienzo de bucle For vacio')

for i in []:
    print('Hola')
    
print('\nFin')

# Ejemplo 3

print('Comienzo de bucle For')

for i in [1,1,1,1]:
    print('Hola estudiantes', end=', ')
    
print('\nFin')

# Ejemplo 4

print('Comienzo de bucle For')

for _i in [0,1,2]:
    print('Hola estudiantes de ingenieria')
    
print('\nFin')

# Ejemplo 5

print('Comienzo de bucle For')

for i in [3,4,5]:
    print(f'Hola, ahora i vale {i} y su cuadrado {i**2}')
    
print('\nFin')

# Ejemplo 6

print('Comienzo de bucle For')

for i in ['Alicia','Wendy','Mauricio','Nestor']:
    print(f'Hola, ahora la variable i vale: {i}\n')
    
print('\nFin')

# Ejemplo 7

print('Comienzo de bucle For')

for num in [0,1,2,3]:
    print(f'{num} * {num} = {num**2}')
    
print('\nFin')

# Ejemplo 8

print('Comienzo de bucle For')

i = 10

print(f'El bucle no ha comenzado, ahora i vale {i}')

for i in [0,1,2,3,4]:
    print(f'{i} * {i} = {i**2}')
    
print(f'El bucle ha terminado, ahora i vale {i}')
    
print('\nFin')

# Ejemplo 9

print('Comienzo del bucle For')

for i in [0,1,2]:
    print(f'{i}*{i}={i**2}')

print('\nOtro bucle For')

for i in [0,1,2,3,4,5]:
    print(f'{i}*{i}={i**2}')

print('Fin')

# Ejemplo 10

palabra = input('Ingresa la palabra a iterar: ')

print('\nComienzo del bucle For')

# for i in 'Fundamentos':
#     print(f'Dame una {i}')
#
# print('Fin')

for i in palabra:
    print(f'Dame una {i}')

print('Fin')

# Ejemplo 11

print('\nComienzo del bucle For')

for i in range(3):
    print('Programacion', end=' ') 

print('Fin')

# Ejemplo 12

print('\nComienzo del bucle For')

for i in range(15):
    print('Hola estudiantes')
    
print('Fin')

# Ejemplo 13

print('\nComienzo del bucle For')

veces = int(input('Cuantas veces quieres que se ejecute el bucle? '))

for i in range(veces):
    print('Estudiantes de programacion')
    
print('Fin')

# Ejemplo 14

print('\nComienzo del bucle For')

for i in range(1,31,6):
    print('Programacion')
    
print('Fin')