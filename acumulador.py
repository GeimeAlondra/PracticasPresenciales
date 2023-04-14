import random

print('Comienza el ejemplo de acumulador')

total = 0

for i in range(3):
    dado3 = random.randrange(1,7)
    print(f'Tiro {i+1}: {dado3}')
    total += dado3

print(f'El total obtenido es de {total} punto(s).')

print('Fin')
