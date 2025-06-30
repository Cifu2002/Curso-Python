""" print("Me gusta ser un módulo 1.")
if __name__ == "__main__":
   print("Prefiero ser módulo.")
else:
   print("Me gusta ser un módulo.") 
contador = 0
   
if __name__ == "__main__":
   print("Prefiero ser un módulo.")
else:
   print("Me gusta ser un módulo.")"""

#!/usr/bin/env python3 
__contador = 0


def suml(the_list):
  global __contador
  __contador += 1
  suma = 0
  for elemento in the_list:
   suma += elemento
  return suma


def prodl(the_list):
  global __contador
  __contador += 1
  prod = 1
  for elemento in the_list:
   prod *= elemento
  return prod


if __name__ == "__main__":
  print("Prefiero ser un módulo, pero puedo hacer algunas pruebas para usted.")
  lista = [i+1 for i in range(5)]
  print(suml(lista) == 15)
  print(prodl(lista) == 120)
  
