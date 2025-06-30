from os import strerror

try:
    contador = 0
    stream = open('archivos\hola.txt', "rt")
    caracteres = stream.read(1)
    while caracteres != '':
        print(caracteres, end='')
        contador += 1
        caracteres = stream.read(1)
    stream.close()
    print("\n\nCaracteres en el archivo:", contador)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))

#lineas
from os import strerror

try:
    character_counter = line_counter = 0
    stream = open('archivos\hola.txt', 'rt')
    line = stream.readline()
    while line != '':
        line_counter += 1
        for char in line:
            print(char, end='')
            character_counter += 1
        line = stream.readline()
    stream.close()
    print("\n\nCaracteres en el archivo:", character_counter)
    print("Líneas en el archivo:     ", line_counter)
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))
    