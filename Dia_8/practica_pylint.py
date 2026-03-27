'''
Módulo para realizar operaciones aritméticas básicas
'''

def sumar():
    '''
    Solicita dos números al usuario y devuelve su suma.
    '''
    numero1 = int(input('Ingrese el número uno: '))
    numero2 = int(input('Ingrese el número dos: '))
    
    resultado = numero1 + numero2
    print(f'El resultado de su suma es {resultado}')
    
    return resultado

if __name__ == '__main__':
    sumar()



