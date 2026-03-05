serie = "N-02"

#if serie == "N-01":
#    print("Samsung")
#elif serie == "N-02":
#    print("Xiaomi")
#elif serie == "N-03":
#    print("Apple")
#else:
#    print("No existe ese producto")

#match serie:
#    case "N-01":
#        print("Samsung")
#    case "N-02":
#        print("Xiaomi")
#    case "N-03":
#       print("Apple")
#    case _:        print("No existe ese producto")

cliente = {"nombre": "Federico", "edad":30, "ciudad": "Madrid"}

pelicula = {"titulo": "Matrix", "ficha_tecnica": {"protagonista": "Keanu Reeves", "director": "Lana Wachowski"}}

elementos = [cliente,pelicula,"libro"]

for e in elementos:
    match e: 
        case {"nombre": nombre,
              "edad" : edad,
              "ciudad": ciudad}:
            print("ES un cliente")
            print(nombre, edad, ciudad)
        case {"titulo": titulo,
              "ficha_tecnica": {"protagonista": protagonista,
                                "director": director}}:
            print("Es una pelicula")
            print(titulo, protagonista, director)
        case _:
            print("No se que es")
        