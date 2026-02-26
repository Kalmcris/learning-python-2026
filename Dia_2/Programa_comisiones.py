#Calculador de comisiones por ventas hechas en el mes
nombre = (input("¿Cuál es su nombre? "))
ventas = (input("¿Cuántas ventas hizo este mes? "))
comision = float(ventas)
comision_final = round(comision*13/100,2)
print (f"Hola {nombre}, su comisión por ventas realizadas este mes son de {comision_final}")
