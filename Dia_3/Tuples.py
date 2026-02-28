mi_tuple =(1,2,3,4)
#mi_tuple[0] = 5 #esto no se puede hacer porque las tuplas son inmutables
print(mi_tuple[-2]) #aquí accedemos al primer elemento de la tupla


mi_tuple = (1,2,(10,20),4)
print(mi_tuple[2][0]) #aquí accedemos al primer elemento de la tupla que está dentro de la tupla principal

t = (1,2,3,1)

print(t.count(1)) #aquí contamos cuántas veces aparece el número 1 en la tupla

mi_lista = list(t) #aquí convertimos la tupla en una lista para poder modificarla