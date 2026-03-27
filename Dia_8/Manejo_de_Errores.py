def suma():
    n1 = int(input('Numero 1: '))
    n2 = int(input('numero 2: '))
    print(n1 + n2 )
    print('Gracias por sumar' + n1)






try: 
    # Codigo que queremos probar
    suma()
except TypeError: 
    #Codigo a ejecutar si no hay error
    print('EStas intentando concatenar tipos distintos')

except ValueError:
    print('Ese no es un numero')
else: 
    #Codigo a ejecutar si no hay un error
    print ('Hiciste todo bien')
finally: 
    #Codigo que se va a ejecutar de todos modos
    print('eso fue todo')