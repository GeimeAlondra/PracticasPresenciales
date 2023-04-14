# Ejemplo testigo

import random

print('Comienza el ejemplo')
sacarCinco = False

for i in range(3):
    dado = random.randrange(1,7)
    print(f'Tiro {i+1}:{dado}')
    if dado == 5:
        sacarCinco = True

if sacarCinco:
    print('Ha salido al menos una vez 5')
else:
    print('No ha salido ningun 5')

print('Fin')

# Otro ejemplo

sacasteCinco = 0

for i in range(5):
    dado2 = random.randrange(1,7)
    print(f'Tiro {i+1}:{dado2}')
    if dado2 == 5:
        sacasteCinco += 1
print(f'En total ha(n) salido {sacasteCinco} cinco')

print('Fin')
