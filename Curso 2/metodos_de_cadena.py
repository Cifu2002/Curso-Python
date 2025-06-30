#Método capitalize() Primera Mayuscula
print('aBcghD'.capitalize())
#Método center() Centra la palabra en un espacio
print('[' + 'alpha'.center(10) + ']')
#Método endswith() Comprueba si el final de la cadena coincide con lo especificado
if "epsilon".endswith("on"):
    print("si")
else:
    print("no")
#Método find() Busca el indice donde aparece la palabra
print("Eta".find("ta"))
print("Eta".find("mma"))
#Método isalnum() Comprueba si es solo digitos o letras
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())
#Método isalpha() Solo letras solamente
print("Moooo".isalpha())
print('Mu40'.isalpha())
#Método isdigit() Busca solo digitos
print('2018'.isdigit())
print("Year2019".isdigit())
#Método islower() Letras si son minúsculas
print("Moooo".islower())
print('moooo'.islower())
#Método isspace() Identifica solo espacios en blancos
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())
#Método isupper()
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())
#Método join() Une los caracteres
print(",".join(["omicron", "pi", "rho"]))
#Método lower() Todas las letras a minusculas
print("SiGmA=60".lower())
#Método lstrip() Elimina los espacios iniciales
print("[" + " tau ".lstrip() + "]")
#Método replace() Pasa un parametro para reemplazar
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))
#Método rfind() Su busqueda es desde el final
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))
#Método rstrip() Afecta al lado opuesto de la cadena 
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))
#Método startswith() Comprueba si la cadena inicia con una subcadena especificada
print("omega".startswith("meg"))
print("omega".startswith("om"))
#Método strip() Elimina los espacios de los extremos
print("[" + "   aleph   ".strip() + "]")
#Método swapcase() Cambia las letras mayusculas a minusculas y biceversa
print("Yo solo sé que no sé nada".swapcase())
#Método title() Primera letra de cada palabra a mayusucla
print("Yo solo sé que no sé nada. Parte 1.".title())
#Método upper() De minusculas a mayusculas
print("Yo solo sé que no sé nada. Parte 2.".upper())
#Metodo similar al split 
def mysplit(strng):
    # Lista para almacenar las palabras
    words = []
    
    # Variable para acumular la palabra actual
    word = ""
    
    # Recorrer cada carácter de la cadena
    for char in strng:
        if char != " ":
            # Si el carácter no es un espacio, lo agregamos a la palabra
            word += char
        else:
            # Si encontramos un espacio y hay una palabra acumulada, la agregamos a la lista
            if word:
                words.append(word)
                word = ""  # Reiniciamos la palabra para la siguiente
    # Al final, si queda una palabra acumulada, la agregamos
    if word:
        words.append(word)
    
    return words

# Probamos la función con los ejemplos dados
print(mysplit("Ser o no ser, esa es la cuestión"))  # ['Ser', 'o', 'no', 'ser,', 'esa', 'es', 'la', 'cuestión']
print(mysplit("   "))  # []
print(mysplit(" abc "))  # ['abc']
print(mysplit(""))  # []
