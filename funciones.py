# Funciones en Python

def Mensaje():
    print('Hola Grupo de Fundamentos de Programación')
    
Mensaje()

def Nombre(nombre):
    print('Hola', nombre)

Nombre('Ana Yancy')

entraNombre = input('Ingresa tu nombre: ')
Nombre(entraNombre)
Nombre(input('Digita otro nombre: '))

def Multiplicar(numero1, numero2):
    print(f'{numero1}*{numero2} = {numero1*numero2}')

print('Comienzo del programa')   
Multiplicar(6,4)
print('Otra forma')
Multiplicar(int(input('Ingrese un numero: ')),int(input('Ingrese otro numero: ')))
print('Fin')

def suma(a,b):
    resultado = a + b
    return resultado

print('El resultado de la suma es: ',suma(8,9))

resultadoSuma = suma(6,4)
print('El resultado de la suma es: ',resultadoSuma)

def es_palindromo(cadena):
    cadena = cadena.lower().replace('a','k')
    print(cadena)
    return cadena == cadena[::-1]

texto = 'Ana lava la tina'
if es_palindromo(texto):
    print('El texto es un palindromo')
else:
    print('El texto no es un palindromo')
    
# Ejemplo de validacion de correo

def validarCorreo():

    email = False

    for i in 'ana@gmail.com':
        if i == '@':
            email = True
            
    if email == True:
        print('El email es correcto')
    else:
        print('El email es incorrecto')
        
def validarCorreo2():
    valido = False
    email = input('Ingrese su correo: ')
    for i in range(len(email)):
        if email[i] == '@':
            valido = True
    if valido == True:
        print('El email es correcto')
    else:
        print('El email es incorrecto')
validarCorreo2()

print('Fin')