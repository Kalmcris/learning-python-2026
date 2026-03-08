#Crear juego ahorcado, programa elegirá una palabra secreta y mostrará guiones
#Si el jugarod dice una letra, el programa rellenará los guiones con la palabra
#Si no existe dicha letra, el juego restará una vida al jugador
#El jugador gana si logra completar la palabra con vidas restantes, de otra manera pierde.

from random import choice

#Intentaré primero crear funciones para cosas específicas y luego lo implementaré
#Funciones como pedir letra, validar letra, chequear letra, ver si ganó, etc 

lista_palabras = ['Linux','Windows','Mac','Android','Iphone','Inteligencia','Emociones']

def elegir_palabra (lista_palabras):
    palabra_elegida = choice(lista_palabras)
    return palabra_elegida

def mostrar_tablero(palabra_elegida):
    for n in palabra_elegida:
        print ('_' , end=' ')

def pedir_letra():
    letra = input('Ingrese una letra: ')
    return letra


def validar_letra(letra):
    letra = letra.lower()
    if not letra.isalpha():
        print('Ingrese una letra válida')
        return False
    elif len(letra) > 1:
        print('Ingrese solo una letra')
        return False
    else:
        return True

def chequear_letra (letra, palabra_elegida):
    if letra in palabra_elegida:
        print('La letra existe en la palabra')
        return True
    else:
        print('La letra no existe en la palabra')
        return False

def jugar_ahorcado():
    palabra_secreta = elegir_palabra(lista_palabras)
    tablero = ['_'] * len(palabra_secreta)
    vidas = 6
    
    while vidas > 0:
        print("\n" + " ".join(tablero))
        
        letra = pedir_letra().lower() # Normalizamos a minúscula
        
        if validar_letra(letra):
            if letra in palabra_secreta.lower():
                # 3. 
                for i in range(len(palabra_secreta)):
                    if palabra_secreta[i].lower() == letra:
                        tablero[i] = palabra_secreta[i]
            else:
                vidas -= 1
                print(f'Esa letra no está. Vidas restantes: {vidas}')
        
        if '_' not in tablero:
            print(f'\n¡Ganaste! La palabra era: {palabra_secreta}')
            return # Terminamos la función
            
    print(f'\nTe quedaste sin vidas. La palabra era: {palabra_secreta}')
jugar_ahorcado()