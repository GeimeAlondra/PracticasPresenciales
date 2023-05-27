from numpy import* 
import numpy as np

x = array([3,4,9,7,2,6,1,5])
print(x)

# Creacion de un arreglo fila
v = array([3,6,7,2,8])
print(v)

# Usando zeros(n)
print(np.zeros(6))

# Usando unos
print(np.ones(6))

# Usando arange(a,b,c)
print(np.arange(3.0,9.0))

# Usando linspace(a,b,c)
print(np.linspace(1,2,5))

a = np.array([55,21,19,11,6])
b = np.array([12,-9,0,22,-9])

#Sumar arreglos
print(a + b)

#Restar arreglos
print(a - b)

# Multiplicar arreglos
print('La multiplicación de los array a * b es: ', a * b)

f = np.array([57,98,-4,5,7])

# Multiplicar por 0.1 todos los elementos del array
print('Esta es la multiplicacion por 0.1: ', 0.1 * f)

# Restar 9 a todos los elementos del array
print('Esta es la resta de 9: ', 9 - f)

# Sumar a todos los elementos del array
print('Esta es la suma de 4: ', 4 - f)

q = np.array([6.2,3.3,4.9,5.1])
w = np.array([5.1,8.7,3.9,3])
e = np.array([5,2,4,4] + np.array([1,4,-2,-1]) / 10.0)

# Operaciones relacionales con arreglos
print(q < w)
print(q == e)

# Usando any
print(any(q < w))
print(any(q == w))

# Usando All
print(all(q == w))

k = [[2,3],[4,5]]
g = [[5,2],[1,4]]

# Concatenar arrays
print(k + g)

# Conversion de una matriz a arreglo
k = np.array(k)
g = np.array(g)

print(k + g)

print(k - g)

print(k * g)

# Funciones especiales
d = np.array([[4,2,5],[2,8,4],[6,9,5]])
print(d)

print(sum(d))

# Producto de todos los elementos
print(prod(d))






