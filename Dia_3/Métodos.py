#upper() - pasar a mayúsculas
#lower() - pasar a minúsculas
#split() - separalo en partes (lista)
#join() - unir items usando separador
#find() - encontrar un sub-string
#replace() - reemplazar un substring

texto = "Este es el texto de Federico"

#resultado = texto.split("t") acá aplicamos el separador "t" y nos devuelve una lista con los elementos separados por ese caracter

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d]) #aquí unimos las palabras usando el espacio como separador
print(e)

#La unica diferencia entre el método find() y el método index() 
# es que el primero devuelve -1 si no encuentra el substring, mientras que el segundo lanza una excepción ValueError.

#texto.replace("e","x") aquí reemplazamos 
# todas las "e" por "x" en el texto original