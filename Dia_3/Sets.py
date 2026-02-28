mi_set = set([1,2,3,4,5,6,5,2,3,4,1,2,3,1,2,3,4,5,6]) #aquí creamos un set a partir de una lista con elementos repetidos
print(type(mi_set)) #aquí verificamos el tipo de dato del set
print(mi_set) #aquí imprimimos el set


#print(mi_set[0]) #esto no se puede hacer porque los sets no tienen índices
print(len(mi_set)) #aquí imprimimos la cantidad de elementos únicos que hay en el set


s1 = {1,2,3,4,5}
s1.add(6) #aquí agregamos un elemento al set
print(s1)

s1.remove(3) #aquí eliminamos un elemento del set
print(s1)

sorteo = s1.pop() #aquí eliminamos un elemento aleatorio del set y lo guardamos en la variable sorteo
print(sorteo)

#unir dos sets = mi_set_3 = mi_set1.union(mi_set2)