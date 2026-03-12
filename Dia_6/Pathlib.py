from pathlib import Path

carpeta = Path('/home/crdev/Documentos/CursoPython/Dia_6/prueba.txt')


#print (carpeta.read_text())
#print(carpeta.name)
#print(carpeta.stem)

if not carpeta.exists():
    print('Este archivo no existe')
else:
    print('Genial, existe')