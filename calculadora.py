import subprocess as sp


def operacion1(n1, n2):
    return n1 + n2


def operacion2(n1, n2):
    return n1 - n2


def operacion3(n1, n2):
    return n1 * n2


def operacion4(n1, n2):
    x = True
    try:
        n1 / n2
    except ZeroDivisionError:
        x = False
    finally:
        if x == True:
            return n1 / n2
        else:
            return 'no se puede dividir'


def mi_menu(argument, n1, n2):
    menu = {
        'suma': operacion1(n1, n2),
        'division': operacion4(n1, n2),
        'resta': operacion2(n1, n2),
        'multiplicacion': operacion3(n1, n2)
    }
    func = menu.get(argument, lambda: "operacion invallida")
    print(func)



bandera = True
while bandera:
    print('digite numero 1:')
    num1 = int(input())
    print('digite numero 2:')
    num2 = int(input())
    print('que desea hacer?')
    operacion = str(input())
    mi_menu(operacion, num1, num2)
    print('seguir si o no?')
    opc = str(input())
    if opc == 'No' or opc == 'no' or opc == '0'or opc == 'N' or opc == 'n':
        bandera = False
    else:
        bandera = True
        tmp = sp.call('cls', shell=True)

