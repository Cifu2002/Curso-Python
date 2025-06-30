try:
    stream = open("C:/Users/Esteban/Desktop/Curso/Curso-Python/Curso 2/archivos/hola.txt", "rt")
    stream.close()
except Exception as exc:
    print("No se puede abrir el archivo:", exc)

import errno

try:
    s = open("archivos/hola.txt", "rt")
    s.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("El archivo no existe.")
    elif exc.errno == errno.EMFILE:
        print("Demasiados archivos abiertos.")
    else:
        print("El numero del error es:", exc.errno)