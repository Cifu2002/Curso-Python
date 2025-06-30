lista1 = []

for ex in range(6):
    lista1.append(10 ** ex)

lista2 = [10 ** ex for ex in range(6)]

print(lista1)
print(lista2)

lista = [1 if x % 2 == 0 else 0 for x in range(10)]

print(lista)