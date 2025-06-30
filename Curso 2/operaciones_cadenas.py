letra1 = 'aa '
letra2 = 'bbb'

print(letra1 + letra2)
print(letra2 + letra1)
print(5 * 'a')
print('b' * 4)

#Saber el codigo ASCII del caracter
char1 = 'a'
char2 = ' '  

print(ord(char1))
print(ord(char2))

#De ASCII a caracter
print(chr(97))
print(chr(32))

# Demonstración de min() 
print(min("aAbByYzZ"))

t = 'Los Caballeros Que Dicen "Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))

# Demonstración de MAX()
print(max("aAbByYzZ"))


t = 'Los Caballeros Que Dicen "Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))

# Método index() 
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

# Función list():
print(list("abcabc1"))

# Función count()
print("abcabc".count("b"))
print('abcabc'.count("d"))
