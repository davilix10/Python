elementos = [8, 3, 1, 19, 14]
n = len(elementos)

for i in range(n-1):       # <-- bucle padre
    print(f"{i+1} Recorrido (i = {i})")
    for j in range(n-1-i): # <-- bucle hijo
        print("j =", j)
        if elementos[j] > elementos[j+1]:
            elementos[j], elementos[j+1] = elementos[j+1], elementos[j]


print(elementos)