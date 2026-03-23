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
    def __init__(self,nombre,apellido, numero_cuenta,balance):
        super().__init__(nombre,apellido)

        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f'Cliente: {self.nombre} {self.apellido}\n, Cuenta: {self.numero_cuenta}\n, Balance: {self.balance}\n'
    
    def depositar(self,cantidad):
        self.balance += cantidad
        print(f'Se han depositado {cantidad} a su cuenta, su nuevo balance es {self.balance}')

    def retirar(self,cantidad):
        if cantidad > self.balance:
            print(f'No es posible hacer ese retiro, pues no cuenta con saldo suficiente.')
        else:
            self.balance -= cantidad
            print(f'Retiro efectuado con éxito, su nuevo saldo es: {self.balance}')
    
def crear_cliente():
    nombre = input('Ingrese su nombre: ')
    apellido = input('Ingrese su apellido: ')
    numero_cuenta = input('Ingrese su número de cuenta: ')
    balance = float(input('Ingrese su balance inicial: '))
    
    cliente = Cliente(nombre, apellido, numero_cuenta,balance)
    return cliente

def inicio():
    cliente = crear_cliente()
    print(cliente)
    while True:
        opcion = input('Ingrese la operación que desea realizar: \n1. Depositar\n2. Retirar\n3. Salir\n')
        if opcion == '1':
            cantidad = float(input('Ingrese la cantidad a depositar: '))
            cliente.depositar(cantidad)
        elif opcion == '2':
            cantidad = float(input('Ingrese la cantidad a retirar: '))
            cliente.retirar(cantidad)
        elif opcion == '3':
            print('Gracias por usar nuestros servicios, hasta luego!')
            break
        else:
            print('Opción no válida, por favor intente de nuevo.')

inicio()