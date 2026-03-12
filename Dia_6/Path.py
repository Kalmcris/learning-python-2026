from pathlib import Path


#base = Path.home()
#guia = Path (base,'Europa','España',Path('Barcelona','Sagrada_Familia.txt'))

#print(guia.parent.parent.parent)

#Para saber todos los .txt en una lista de directorios de carpetas
#guia = Path(Path.home(),'Europa')

#for txt in Path(guia).glob('**/*.txt'):
 #   print(txt)

guia = Path('Europa','españa','Barcelona','Sagrada_Familia.txt')
en_europa = guia.relative_to(Path('Europa'))
en_espania = guia.relative_to(Path('Europa','España'))
print(en_europa)
print(en_espania)
