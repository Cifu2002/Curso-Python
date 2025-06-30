lista = [1 if x % 2 == 0 else 0 for x in range(10)]
generador = (1 if x % 2 == 0 else 0 for x in range(10))

for v in lista:
    print(v, end=" ")
print()

for v in generador:
    print(v, end=" ")
print()

