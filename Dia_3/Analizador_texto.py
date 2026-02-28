#Crear un programa analizador de texto, le pediré al usuario una frase, texto etc
#Luego, le pediré al usuario que ingrese tres letras a su elección
#Y el programa deberá decirme cuantas veces aparece cada letra, cuántas palabras hay en total,
#Primera y última letra, palabras en orden inverso, y por último si aparece la palabra
#Python

#Primera información: cuantas veces aparece cada letra
frase = input("Ingrese una frase: ")

letra1 = input("Ingrese la primera letra: ")    
letra1_minuscula = letra1.lower() 

letra2 = input("Ingrese la segunda letra: ")
letra2_minuscula = letra2.lower()

letra3 = input("Ingrese la tercera letra: ") 
letra3_minuscula = letra3.lower()
frase_en_minusculas = frase.lower()


print(f"La letra {letra1_minuscula} aparece {frase_en_minusculas.count(letra1_minuscula)} veces")
print(f"La letra {letra2_minuscula} aparece {frase_en_minusculas.count(letra2_minuscula)} veces")
print(f"La letra {letra3_minuscula} aparece {frase_en_minusculas.count(letra3_minuscula)} veces")

#Segunda información: cuántas palabras hay en total
palabras = frase.split()
palabras_contados = len(palabras)
print (f"En total hay {palabras_contados} palabras en la frase ingresada.")

#Tercera información: Primera y última letra
primera_letra = frase[0]
ultima_letra = frase[-1]
print(f"La primeta letra de la frase es {primera_letra} y la ultima letra de la frase es {ultima_letra}.")

#Cuarta información: palabras en orden inverso
palabras_invertidas = palabras[::-1]
palabras_invertidas_unidas = " ".join(palabras_invertidas)
print(f"Las palabras en orden inverso son: {palabras_invertidas_unidas}")

#Quinta información: ¿Aparece la palabra Python? 
buscar_python = "python" in frase_en_minusculas
dic = {True: "Sí", False : "No"}
print(f"¿Aparece la palabra Python en la frase? {dic[buscar_python]}")

