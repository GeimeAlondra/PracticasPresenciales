precioProducto =float(input('\nIngrese el costo del articulo: '))

cantidadDinero = float(input('\nIngrese la cantidad de dinero que entregó el cliente: '))

if cantidadDinero > precioProducto:
    
    cambio = cantidadDinero - precioProducto
    print('\nSu cambio es de: ', cambio, 'dolares')

elif cantidadDinero == precioProducto:
    
    print('\nSe ha pagado exacto, no es necesario dar cambio')

elif cantidadDinero < precioProducto:
    
    faltante = precioProducto - cantidadDinero
    print('\nEl cliente debe: ', faltante, 'dolares')

else:
    print('\nLos datos ingresados no son validos')