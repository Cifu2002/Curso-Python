from platform import platform, machine, processor
#datos sobre el so
print(platform())
print(platform(1))
print(platform(0, 1))
#Procesador nombre generico
print(machine())
#Procesador nombre especifico si es posible
print(processor())