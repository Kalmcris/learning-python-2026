#Escribir una función que requiera una cantidad indefinida de argumentos
#LO que hará la función es devolver True si en algun momento
#se ingresa el numero 0 dos veces consecutivas
def cero_repetido(*args):
    for i in range(len(args)-1):
        if args[i] == 0 and args[i+1] == 0:
            return True
    return False
    
print(cero_repetido(1,2,3,4))