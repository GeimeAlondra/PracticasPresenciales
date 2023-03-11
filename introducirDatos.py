# Introducir datos desde teclado

# Cadena string

palabras = input("Ingrese una palabra:")
otraVariable = "Alunmos de Fundamentos de Progrmacion"

print("Esto es el string que hemos solicitado al usuario: ", palabras)
print("Esto es el string: "+ palabras + " " + "Aqui se puede agregar mas información" + otraVariable + " " + "solo hay que concatenar")

#Enteros

numInt = int(input("Introduce un numero entero: "))
print("Este es el numero dado por el usuario: ", numInt)

# Flotante

numFloat = float(input("Introduce un numero decimal: "))
print("Este es el numero decimal dado por el usuario: ", numFloat)

# Complejos

numComp =complex(input("Introduce un numero complejo: "))
print("Esto es un numero complejo: ", numComp)
