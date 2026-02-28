mi_lista = ["a", "b", "c"]
mi_lista2 = ["d", "e", "f"]

resultado = len(mi_lista) #Vemos cantidad de elementos que tiene la lista, en este caso devuelve 3
print(resultado)
print(type(mi_lista)) #devuelve el tipo de dato de mi_lista, que es <class 'list'>

mi_lista3 = mi_lista + mi_lista2 #aquí concatenamos las dos listas
print(mi_lista3)


mi_lista3[0] = "x" #aquí cambiamos el primer elemento de la lista por "x"
print(mi_lista3)

mi_lista3.append("g") #aquí agregamos un nuevo elemento al final de la lista
print(mi_lista3)

eliminado   = mi_lista3.pop(0) #aquí eliminamos el último elemento de la lista
print(mi_lista3)

print(eliminado)

lista_desordenada = ["z", "a", "c", "b"]
lista_desordenada.sort() #aquí ordenamos la lista de forma alfabética
print(lista_desordenada)