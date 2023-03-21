print('Conversor')

print('Menu de opciones:\n')
print('Presione 1 para convertir de numeros a palabras ')
print('Presione 2 para convertir de palabras a numeros \n')

opcion = int(input('Cual es la opcion que desea seleccionar? '))

if opcion == 1:
    print('Conversor de numeros a palabras')

    opcionNumero = int(input('Cual es el numero que desea convertir a palabra? '))
    if opcionNumero == 1:
        print('El numero es UNO')
    elif opcionNumero == 2:
        print('El numero es DOS')
    elif opcionNumero == 3:
        print('El numero es TRES')
    elif opcionNumero == 4:
        print('El numero es CUATRO')
    elif opcionNumero == 5:
        print('El numero es CINCO')
    else:
        print('El numero ingresado no se puede convertir')

elif opcion == 2:
    print('Conversor de palabras a numeros')

    opcionPalabra = input('Cual es la palabra que desea convertir en numero? ')
    if opcionPalabra == 'uno':
        print("La palabra es '1'")
    elif opcionPalabra == 'dos':
        print("La palabra es '2'")
    elif opcionPalabra == 'tres':
        print("La palabra es '3'")
    elif opcionPalabra == 'cuatro':
        print("La palabra es '4'")
    elif opcionPalabra == 'cinco':
        print("La palabra es '5'")
    else:
        print('La palabra ingresada no se puede convertir')

else:
    print('La opcion ingresada no es correcta')


