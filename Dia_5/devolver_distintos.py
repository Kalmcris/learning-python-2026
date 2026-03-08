#Crear una función llamada devolver_distintos() que reciba 3 integers
#cómo parametros

def devolver_distintos(num1,num2,num3):
    valor = sum(num1,num2,num3)
    numeros = [num1,num2,num3]
    if valor > 15:
        return max(numeros)
    elif valor <10:
        return min(numeros)
    else:
        numeros.sort()
        return numeros[1]