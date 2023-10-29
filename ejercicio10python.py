barras = int(input('Cuantas barras de pan que no son del dia se han vendido?' ))
precio = 3.49
descuento = 0.6
coste = barras * precio * (1 - descuento)
print('El precio normal de una barra hecha hoy es de: ', precio, '€')
print('El descuento de una barra no hecha hoy es de: ', (descuento * 100), '%')
print('El coste total es de: ', round(coste, 3), '€')