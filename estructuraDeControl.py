# Estructura IF o Sentencia simple

print ("Sistema para calcular el promedio de un alumno")
nombre = input("Para comenzar, ¿Cual es tu nombre?")

fdp = int(input(nombre + " " + "¿Cual es tu calificación en Fundamentos de Programación?"))
mat1 = int(input(nombre + " " + "¿Cual es tu calificación en Matemática I?"))
lfg = int(input(nombre + " " + "¿Cual es tu calificación en Liderazgo y Funviones Gerenciales?"))
oti = int(input(nombre + " " + "¿Cual es tu calificación en Orientación Tecnica de Ingenieria?"))
ing = int(input(nombre + " " + "¿Cual es tu calificación en Ingles?"))
psg = int(input(nombre + " " + "¿Cual es tu calificación en Psicologia General?"))

promedio = (fdp + mat1 + lfg + oti + ing + psg) / 6

print(nombre + " " + "Tu promedio es: ", promedio)

if promedio >= 6:
    print("Felicidades", nombre + " " + "Aprobaste con un promedio de: ", promedio)
    
print("Fin")

variableString = "'Esto resalta' el texto"
variableString1 = '"Esto resalta" el texto'
print(variableString)
print(variableString1)