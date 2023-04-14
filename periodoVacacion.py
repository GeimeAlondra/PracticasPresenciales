print('*******************************')
print('Sistema de cotrol de vacaciones')
print('*******************************')

nombreEmpleado = str(input('Poor favor, introduce tu nombre: '))
print('Claves de departamento\n 1. Atencion al cliente\n 2. Ventas\n 3. Gerencia')
clave = int(input('Por favor, introduce la clave del departamento: '))
añoServicio = int(input('Por favor, introduce tus años de servicio: '))

if clave == 1:
    
    if añoServicio == 1 and añoServicio < 2:
        print('El empleado', nombreEmpleado, 'tiene derecho a 6 dias de vacaciones')
    elif añoServicio >= 2 and añoServicio <= 6:
        print('El empleado', nombreEmpleado, 'tiene derecho a 14 dias de vacaciones')
    elif añoServicio >= 7:
        print('El empleado', nombreEmpleado, 'tiene derecho a 20 dias de vacaciones')
    else:
        print('Aun no cumples un año de servicio')

elif clave == 2:
    
    if añoServicio == 1 and añoServicio < 2:
        print('El empleado', nombreEmpleado, 'tiene derecho a 7 dias de vacaciones')
    elif añoServicio >= 2 and añoServicio <= 6:
        print('El empleado', nombreEmpleado, 'tiene derecho a 15 dias de vacaciones')
    elif añoServicio >= 7:
        print('El empleado', nombreEmpleado, 'tiene derecho a 22 dias de vacaciones')
    else:
        print('Aun no cumples un año de servicio')

elif clave == 3:
    
    if añoServicio == 1 and añoServicio < 2:
        print('El empleado', nombreEmpleado, 'tiene derecho a 10 dias de vacaciones')
    elif añoServicio >= 2 and añoServicio <= 6:
        print('El empleado', nombreEmpleado, 'tiene derecho a 20 dias de vacaciones')
    elif añoServicio >= 7:
        print('El empleado', nombreEmpleado, 'tiene derecho a 30 dias de vacaciones')
    else:
        print('Aun no cumples un año de servicio')

else:
    print('La opcion ingresada no existe, vuelva a intentarlo')
