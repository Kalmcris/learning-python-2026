""""
monedas = 5

while monedas > 0:
    print (f"Te quedan {monedas} monedas")
    monedas -= 1
else: 
    print("Ya no te quedan monedas")    
    """

nombre = input("Introduce tu nombre: ")
for letra in nombre:
    if letra == "r":
        break
    print (letra)