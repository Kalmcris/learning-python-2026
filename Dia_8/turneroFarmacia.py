#Creacion de un turnero para una farmacia, con 3 áreas de atención diferentes, perfumeria, farmacia y cosméticos. 
#El programa debe preguntar al cliente a cuál area se dirigirá y le va a dar un número 
#Son diferentes órdenes de números para cada área. ejemplo, su turno es: C-54, esto indica que va a cosméticos y tiene el turno 54. 
#Intentar usar decoradores. 


def numeros_perfumeria():
    for n in range(1,1000):
        yield

def numeros_farmacia():
    for n in range(1,1000):
        yield

def numeros_cosmeticos():
    for n in range(1,1000):
        yield

p = numeros_perfumeria()
f = numeros_farmacia()
c = numeros_cosmeticos()


def decorador(rubro):

    print ('\n' + '*'*20)
    print('Su turno es: ')
    if rubro == 'P':
        print(next(p))
    elif   rubro == 'F':
        print(next(f))  
    else:
        print(next(c))
    print('Aguarde y será atendido')
    print('*'*20 + '\n')

def preguntar():

    print('Bienvenido al turnero de la farmacia, por favor indique a cuál área se dirigirá: ')
    
    while True: 
        print ('[P] - Perfumería\n[F] - Farmacia\n[C] - Cosméticos\n[X] - Salir')
        try:
            mi_rubro = input('Elija su rubro: ').upper
            ['P','F','C','X'].index(mi_rubro)
        except: 
            print('Esa no es una opción valida, intente nuevamente')
        else:
            break
    
    decorador(mi_rubro)

def inicio():
    while True:
        preguntar()
        try:
            otro_turno = input('¿Desea sacar otro turno? [S/N]: ').upper()
            ['S','N'].index(otro_turno)
        except:
            print('Esa no es una opción valida, intente nuevamente')
        else:
            if otro_turno == 'N':
                print('Gracias por usar el turnero, vuelva pronto!')
                break

inicio()