dic = {"c1":["a","b","c"], "c2":["d","e","f"]}

print(dic["c2"][1].upper()) #aquí accedemos al segundo elemento de la lista asociada a la clave "c2" y lo convertimos a mayúscula


dic2={1:"a",2:"b"}
dic2[3] = "c" #aquí agregamos un nuevo par clave-valor al diccionario
print(dic2)

dic2[2] = "B" #aquí modificamos el valor asociado a la clave 2
print(dic2)

print(dic.keys()) #aquí obtenemos una vista de las claves del diccionario
print(dic.values()) #aquí obtenemos una vista de los valores del diccionario
print(dic.items()) #aquí obtenemos una vista de los pares clave-valor del diccionario