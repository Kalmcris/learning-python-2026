#Crear clase Persona con atributos: Nombre y apellido
#Crear clase cliente (hereda de persona), además tiene atributos, numero de cuenta y balance
#cliente tiene métodos, método especial de imprimir a nuestro cliente, todos sus datos
#Método depositar, que permite añadir a su cuenta y método retirar, para retirar dinero de su cuenta
#Código para elegir depositar, retirar o salir, cuantas operaciones quiera hasta salir. cliente no puede retirar más dinero del que tiene. 
#Crear funciones crear_cliente() y crear función de inicio. 

class Persona():
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self,nombre,apellido,numero_cuenta,balance):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f'CLiente: {self.nombre} {self.apellido}\nBalance de cuenta {self.numero_cuenta}: ${self.balance}'
    

    def depositar(self,monto_deposito):
        self.balance += monto_deposito
        print('Deposito aceptado')
    
    def retirar(self,monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -=monto_retiro
            print('Retiro realizado')
        
        else:
            print('Fondos insuficientes')


def crear_cliente():
    nombre_cl = input('Ingrese su nombre: ')
    apellido_cl = input('Ingrese su apellido ')
    numero_cuenta = input('Ingrese su numero de cuenta: ')
    balance = 0
    cliente = Cliente(nombre_cl, apellido_cl, numero_cuenta,balance)
    return cliente

def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)

    opcion = 0

    while opcion != 'S':
        print('Elige: Depositar (D), Retirar (R), o Salir(S)')
        opcion = input()

        if opcion == 'D':
            monto_dep = int(input('Monto a depositar: '))
            mi_cliente.depositar(monto_dep)

        elif opcion == 'R':
            monto_ret = int(input('Monto a retirar: '))
            mi_cliente.retirar(monto_ret) 
        print(mi_cliente)

    print('Gracias por operar en Banco BCI')
            

inicio()