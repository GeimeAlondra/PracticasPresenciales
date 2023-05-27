cadena1 = 'Tengo una gatita que se llama Luna' # Declaracion de variable
print(cadena1)

# lista1 = [] # Lista vacia

lista1 = ['Pera','Manzana','Uva'] # Declaracion de una lista
print(lista1)

longitud = len(cadena1) # # Devuelve la longitud de la cadena
print(longitud)

elementos = len(lista1) # Devuelve el numero de elementos de la lista
print(elementos)

cuenta = cadena1.count('Luna') # Cuenta cuantas veces aparece la palabra Luna
print(cuenta)
print(cadena1.find('Luna')) # Devuelve la posicion de busqueda

cadena2 = cadena1.join('**') # Inserta 
print(cadena2)

lista2 = cadena1.split(' ') # Divide la cadena por cada espacio
print(lista2)

cadena3 = cadena1.replace('a','o',5) # Busca y sustituye cuantas veces sea necesario
print(cadena3)

cadena4 = 'Mar' # Variable mAr maR MAR Mar
print(cadena4.upper()) # Convierte a mayusculas
print(cadena4.lower()) # Convierte a minusculas 
print(cadena4.capitalize()) # Convierte la primera letra en mayuscula

lista3 = ['Fundamentos',2,True,2.2] # Lista heterogenes
print(lista3)
print(lista3[0])

lista4 = [1,2,3,4] # Lista homogenea
print(lista4)
print(lista4[-1])

lista5 = ['nombre'['Tel','direc']] # Declara lista de otra lista
print(lista5)
print(lista5[1][0])

print(lista4)[1:3:1] # Responde al patron inicio:fin:paso
print(lista4[1][1:5:2]) # La posicion inicio:fin:paso

lista3[2] = False # Cambieamos el valor de un elemento de la lista
print(lista3)

lista4[-2] = lista4[-2] + 1
print(lista4)
lista4[-3] = lista4[-3] - 1
print(lista4)

lista4.pop(0)
print(lista4)

lista3.REMOVE("Fundamentos") 
print(lista3)

lista3 = lista3 + [6]
print(lista3)

lista3.append(7)
print(lista3)

lista3.extend([8,9])
print(lista3)

lista3.insert(1,"Programacion")
print(lista3)

lista3[:] = []
print(lista3)
print(lista1.count(2))
print(lista1.index("Uva"))