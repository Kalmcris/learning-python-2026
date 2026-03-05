from random import *

#Me entrega un numero entero aleatorio entre 1 y 50
#aleatorio = randint(1,50)
#print(aleatorio)

#Me entrega un numero decimal aleatorio entre 1 y 5, con 2 decimales
#aleatorio = round(uniform(1,5),2)
#print(aleatorio)

#Me entrega un numero decimal aleatorio entre 0 y 1
#aleatorio = random()
#print(aleatorio)

#Me entrega un elemento aleatorio de la lista
#colores = ["azul", "rojo", "verde", "amarillo"]
#aleatorio = choice(colores)
#print(aleatorio)

#Me mezcla los elementos de la lista de forma aleatoria
numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)

