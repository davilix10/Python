peso = input('Cuanto pesas? ')
altura = input('Cuanto mide? ')
imc = round(float(peso) / float(altura) ** 2,2)
print('Tu indice de masa corporal es de '+ str(imc))