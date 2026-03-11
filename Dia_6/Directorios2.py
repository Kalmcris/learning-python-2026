from pathlib import Path

carpeta = Path('/home/crdev/Documentos/CursoPython/Dia_6')

archivo = 'prueba.txt'

mi_archivo = open(archivo)

print(mi_archivo.read())