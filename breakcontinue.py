# Ejemplo para break

print('While con sentencia break')

contador = 0

while contador < 10:
    contador += 1
    if contador == 5:
        break
    print('Valor actual de la variable: ', contador)
    
print('Fin del programa, la sentencia break se ha ejecutado')

# Ejemplo para continue

print('While con sentencia continue')

cont = 0

while cont < 10:
    cont += 1
    if cont == 5:
        continue
    print('Valor actual de la variable: ', cont)
    
print('Fin del programa, la sentencia continue se ha ejecutado')