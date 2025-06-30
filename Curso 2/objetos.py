#pila como objeto 
class pila:  # Definiendo la clase pila.
    def __init__(self):  # Definiendo la función del constructor.
        print("¡Hola mundo cruel twt!")


pila_objecto = pila()  # Instanciando el objeto.

class pila1:
    def __init__(self):
        self.__pila1_lista = []


    def push(self, val):
        self.__pila1_lista.append(val)


    def pop(self):
        val = self.__pila1_lista[-1]
        del self.__pila1_lista[-1]
        return val
pila_objeto = pila1()

pila_objeto.push(3)
pila_objeto.push(2)
pila_objeto.push(1)

print(pila_objeto.pop())
print(pila_objeto.pop())
print(pila_objeto.pop())