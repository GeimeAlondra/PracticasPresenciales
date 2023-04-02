num1 = int(input('\nIngrese el primer número: '))

num2 = int(input('\nIngrese el segundo número: '))

num3 = int(input('\nIngrese el tercer número: '))

# Numero mayor
if num1 > num2 and num1 > num3:
    mayor = num1
elif num2 > num1 and num2 > num3:
    mayor = num2
elif num3 > num1 and num3 > num2:
    mayor = num3
else:
    print('Error')

# Numero menor 
if num1 < num2 and num1 < num3:
    menor = num1
elif num2 < num1 and num2 < num3:
    menor = num2
elif num3 < num1 and num3 < num2:
    menor = num3
else:
    print('Error')
    
# Numero medio 
if num1 != mayor and num1 != menor:
    medio = num1
elif num2 != mayor and num2 != menor:
    medio = num2
else:
    medio = num3
    
print('\nEl número', mayor, 'es el número más grande de los tres')
print('\nEl número', medio, 'es el número medio de los tres')
print('\nEl número', menor, 'es el número más pequeño de los tres')

