diccionario={
    'juego':'fortnite', 
    'creacion':2019,
    'creador':'epic games'
}
print(diccionario['juego'])

print("-"*96)

print(diccionario)
diccionario.update({'juego': 'fornile'})
print(diccionario)

print("-"*96)

print(diccionario)
diccionario['creador']='david'
print(diccionario)

print("-"*96)

print(diccionario)
diccionario['doramion']='a'
print(diccionario)

print("-"*96)

print(diccionario)
diccionario.pop('creacion')
print(diccionario)

print("-"*96)

print(diccionario)
diccionario.setdefault('creacion', 2020)
print(diccionario)

print("-"*96)

print(diccionario)
diccionario.clear()
print(diccionario)
