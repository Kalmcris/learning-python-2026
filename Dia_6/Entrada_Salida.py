mi_archivo = open("prueba.txt")

#una_linea = mi_archivo.readline()
#print(una_linea.upper())

#una_linea = mi_archivo.readline()
#print(una_linea.lower())

#una_linea = mi_archivo.readline()
#print(una_linea.upper())

#for l in mi_archivo:
#    print("Aquí dice: " + l)

todas = mi_archivo.readlines()

todas = todas.pop()

print(todas)