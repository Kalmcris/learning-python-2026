num1 = 5.8
print(num1)
print(type(num1))

#Lo connvierte, simplemente elimina la decimal
num2 = int(num1)
print(num2)
print(type(num2))

edad = input("Dime tu edad: ")
edad = int(edad)

#esta parte arrojará error pues solo se pueden concatenar integers.
nueva_edad = 1 + edad
print(nueva_edad)
print ("Tu nueva edad va a ser " + nueva_edad)
