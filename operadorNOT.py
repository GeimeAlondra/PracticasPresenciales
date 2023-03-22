print('Operador NOT')

numN = int(input('Digite un numero: '))

if not numN > 5:
    print('La condicion se invirtio y se cumple al ser un numero menor que 5')
else:
    print('No se completo la condicion porque el numero es mayor que 5')
    
if not numN < 5:
    print('La condicion se invirtio y se cumple al ser un numero mayor que 5')
else:
    print('No se completo la condicion porque el numero es menor que 5')

print('Fin')