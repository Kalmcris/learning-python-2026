nombres = ["Juan", "María", "Pedro"]
edades = [25, 30, 35]
ciudades = ["Madrid", "Barcelona", "Valencia"]


combinados = list(zip(nombres, edades,ciudades))

for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}.")




