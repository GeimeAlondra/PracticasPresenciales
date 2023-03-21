# Este es un ejemplo de condicional compuesto
print("Sistema para calcular el promedio de alumnos")
nombre = input("Danos tu nombre: ")

mate = float(input(nombre + " " + "¿Cual es tu nota en matematicas?"))
fisica = float(input(nombre + " " + "¿Cual es tu nota en fisica?"))
biologia = float(input(nombre + " " + "¿Cual es tu nota en biologia?"))

promedio = (mate + fisica + biologia) / 3

if promedio >= 6:
    print("Felicidades "+ nombre + " " + "aprobaste con un promedio de: ", promedio)
    print("Felicidades "+ nombre + " " + "aprobaste con un promedio de: ", round(promedio)) 

else:
    print("Lo sentimos "+ nombre + " " + "has 'reprobado' con un promedio de ", promedio)
    print("Lo sentimos "+ nombre + " " + "has 'reprobado' con un promedio de ", round(promedio))
    
print("FIN")