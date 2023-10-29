edad = int(input('Cuantos años tienes? '))
if edad <= 5:
    print('Vete a la cuna nene')
elif edad >= 6 and edad <= 17:
    print('Eres menor de edad')
elif edad >= 18 and edad <= 29:
    print('Eres mayor de edad, vete a beber')
elif edad >= 30 and edad <= 50:
    print('Eres mas mayor, el niño para cuando?')
elif edad >= 50 and edad <= 80:
    print('Te haces mayor, para cuando la boda')
elif edad >= 80 and edad <= 100:
    print('Eres un viejo ya, vete a la residencia')
else:
    print('A ver quien dura mas')