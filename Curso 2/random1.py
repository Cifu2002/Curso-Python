from random import random, seed, randint, choice, sample
seed(0) #la semilla de aleatoriedad se establece en el mismo numero por lo que ya no es random
#solo seed() usa la hora actual

for i in range(5):
    print(random())

for i in range(5): #numeros ranoms enteros 
    print(randint(1,10),end=',')

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('choice y sample')
print(choice(lista)) #Elige un elemento de la lista
print(sample(lista, 5)) #Elige 5 elementos de la lista
print(sample(lista, 10)) #Elige 10 elementos de la lista
from random import randint
    
for i in range(2):
   print(randint(1, 2), end='')

    