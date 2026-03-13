#Crear administrador de rectas, usando a su vez los directorios que se encuentran en Recetas.
#Debe dar un saludo de bienvenida, decir donde están las recetas, cuántas recetas hay, luego mostrar un menú con las siguientes opciones:
#1. Leer receta: con esta debe elegir categoria, mostrar recetas y luego elegir la receta a mostrar
#2. Agregar receta: con esta, debe elegir la categoria, escribir el nombre y crear el contenido de la receta
#3. Crear categoría: debe elegir nombre de categoria y crear la carpeta
#4. eliminar receta: debe elegir categoria, mostras las recetas y elegir la receta para eliminarla
#5. eliminar categoría: Elegir categoria y eliminar la carpeta con todo su contenido
#6. Salir
#Algunas consideraciones son envolar las opciones en loop while, así se repiten hasta que el usuario decida retroceder o salir 
#usar system clear para limpiar la consola
#Compartimentar el código en funciones para cada opción del menú, así el código es más organizado y fácil de leer
import os 
from pathlib import Path
import subprocess

mi_ruta = Path(Path.home(), "Documentos", "CursoPython", "Dia_6", "Recetas")



def contar_recetas(ruta):
    contador = 0
    for _ in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador


def inicio():
    subprocess.run(['clear'])
    print ('*'*50)
    print ('*' *5 +' Bienvenido al administrador de recetas '+ '*' *5 )
    print ('*'*50)
    print('\n')
    print(f'Las recetas se encuentran en {mi_ruta}')
    print(f'Actualmente hay {contar_recetas(mi_ruta)} recetas disponibles')

    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in [1, 2, 3, 4, 5, 6]:
        print('Elige una opción del menú:')
        print('1. Leer receta')
        print('2. Agregar receta')
        print('3. Crear categoría')
        print('4. Eliminar receta')
        print('5. Eliminar categoría')
        print('6. Salir')
        eleccion_menu = input('Opción: ')
        
    # El return debe ir FUERA del while y convertido a entero
    return int(eleccion_menu)


def mostrar_categorias(ruta):
    print('Categorías disponibles:')
    ruta_catregorias = Path(ruta)
    lista_categorias = []
    contador = 1
    for carpeta in ruta_catregorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f'[{contador}] - {carpeta_str}')
        lista_categorias.append(carpeta_str)
        contador += 1
    return lista_categorias


def elegir_categoria(lista):
    eleccion_correcta = 'x'
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input('\nElige una categoría: ')
        
    # Fuera del while
    return lista[int(eleccion_correcta) - 1]

def mostrar_recetas(ruta):
    print('Recetas:')
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1
    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f'[{contador}] - {receta_str}')
        lista_recetas.append(receta)
        contador += 1
    return lista_recetas

def elegir_recetas(lista):
    eleccion_correcta = 'x'

    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input('\nElige una receta: ')

        return lista[int(eleccion_correcta) - 1]

def leer_receta(receta):
    print(Path.read_text(receta))

def crear_receta(ruta):
    existe = False
    while not existe:
        print('Escribe el nombre de tu receta: ')
        nombre_receta = input() + '.txt'
        print('Escribe tu nueva receta: ')
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, input())
            print (f'Tu receta {nombre_receta} ha sido creada con éxito')
            existe = True
        else:
            print('Ya existe una receta con ese nombre, elige otro nombre para tu receta')
        
def crear_categoria(ruta):
    existe = False
    while not existe:
        print('Escribe el nombre de tu categoría: ')
        nombre_categoria = input() + '/'
        print('Escribe tu nueva categoría: ')
        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print (f'Tu categoría {nombre_categoria} ha sido creada con éxito')
            existe = True
        else:
            print('Ya existe una categoría con ese nombre, elige otro nombre para tu categoría')
        
def eliminar_receta(receta):
    Path(receta).unlink()
    print(f'La receta {receta} ha sido eliminada con éxito')

def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f'La categoría {categoria} ha sido eliminada con éxito')

def volver_inicio():
    eleccion_regresar = 'x'
    while eleccion_regresar.lower() not in ['s', 'n']:
        eleccion_regresar = input('¿Deseas volver al menú principal? (s/n): ')
        if eleccion_regresar.lower() == 's':
            return True
        elif eleccion_regresar.lower() == 'n':
            return False
        else:
            print('Opción no válida, por favor elige "s" para sí o "n" para no.')


finalizar_programa = False
while not finalizar_programa:
    menu = inicio()

    if menu == 1:
        mis_categorias = mostrar_categorias(mi_ruta)
        elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_ruta)
        mi_receta =elegir_recetas(mis_recetas)
        leer_receta(mi_receta)
        volver_inicio()
        pass
    elif menu == 2:
        mis_categorias = mostrar_categorias(mi_ruta)
        elegir_categoria(mis_categorias)
        crear_receta(mis_categorias)
        volver_inicio()
        pass
    elif menu == 3:
        crear_categoria(mi_ruta)
        volver_inicio()
        pass
    elif menu == 4:
        mis_categorias = mostrar_categorias(mi_ruta)
        elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_ruta)
        mi_receta =elegir_recetas(mis_recetas)
        eliminar_receta(mi_receta)
        volver_inicio()
        pass
    elif menu == 5:
        mis_categorias = mostrar_categorias(mi_ruta)  #Mostrar categorias
        elegir_categoria(mis_categorias)
        eliminar_categoria(mis_categorias)
        volver_inicio()
        pass
    elif menu == 6:
        finalizar_programa = True
        pass