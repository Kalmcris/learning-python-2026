def letras_unicas(palabra):
    letras_limpias = set(palabra)
    lista_ordenada = sorted(letras_limpias)
    return lista_ordenada
    
print(letras_unicas("cascarrabias"))