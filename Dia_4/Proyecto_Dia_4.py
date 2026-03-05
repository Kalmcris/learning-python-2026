#Juego de adivinar el número, el programa dará un numero de intentos para 
#adivinar el número, el programa dará pistas si el número es mayor o menor al número a adivinar
#Empezaré diciendo que el numero es entre 1 y 100, si el usuario da un numero fuera de ese rango dará un mensaje de error y no contará como intento
#Si es menor, el programa dirá que es incorrecto y que el número es mayor, si es mayor, el programa dirá que es incorrecto y que el número es menor
#Si el usuario adivina el número, el programa dirá que es correcto y mostrará el número de intentos que le tomó adivinar el número
#Si el usuario no adivina el número en el número de intentos, el programa dirá que ha perdido y mostrará el número a adivinar
import random
adivinar_numero = random.randint(1, 100)
print(("Bienvenido al juego de adivinar el número, el número a adivinar está entre 1 y 100," \
" Cuántos intentos quieres tener? "))
intentos = int(input())

for i in range(intentos):
    print (f"Intento número {intentos-i}")
    numero_usuario = int(input("Ingresa un número: "))
    if numero_usuario < 1 or numero_usuario > 100:
        print("Número fuera de rango, por favor ingresa un número entre 1 y 100")
        continue
    if numero_usuario < adivinar_numero:
        print("Incorrecto, el número es mayor")
    elif numero_usuario > adivinar_numero:
        print("Incorrecto, el número es menor")
    else:
        print(f"Correcto, has adivinado el número {adivinar_numero} en {i+1} intentos")
        break
else:
    print(f"Has perdido, el número a adivinar era {adivinar_numero}, buen intento!")