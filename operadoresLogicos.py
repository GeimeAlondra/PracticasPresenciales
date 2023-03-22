print('Introduce dos numeros a comparar: ')

numUno = int(input('Introduce el primer numero: '))
numDos = int(input('Introduce el segundo numero: '))

print('\n Los números a comparar son: ', numUno, 'y', numDos,'\n')
print('\n Los números a comparar son: ' + str(numUno) + 'y' + str(numDos) + '\n')

if numUno == numDos:
    print('Los números son iguales...')
if numUno != numDos:
    print('Los números son diferentes...')
if numUno > numDos:
    print('Es mayor')
if numUno < numDos:
    print('Es menor')
if numUno >= numDos:
    print('Es mayor o igual...')
if numUno <= numDos:
    print('Es menor o igual...')