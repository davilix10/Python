invertir = float(input('Cantidad a invertir '))
interes = float(input('Interes porcental anual '))
anos = int(input('Numero de años '))
print("Dinero final = " + str(round(invertir * (interes/100+1)**anos, 2)))