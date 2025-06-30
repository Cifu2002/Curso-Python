primer_numero = int(input("Ingresa el primer número: "))
segundo_numero = int(input("Ingresa el segundo numero: "))

try:
    print(primer_numero / segundo_numero)
except:
    print("Esta operación no puede ser realizada.")

print("FIN.")

#TRY y Except
try:
    print("1")
    x = 1 / 0
    print("2")
except:
    print("Oh cielos, algo salió mal...")

print("3")

#Raise
def bad_fun(n):
    raise ZeroDivisionError


try:
    bad_fun(0)
except ArithmeticError:
    print("¿Qué pasó? ¿Un error?")

print("FIN.")
    
    
    