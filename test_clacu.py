import subprocess as sp

def test_operacion1(n1, n2):
    return n1 + n2 #para el testing se debe probar las funciones individualmente


def test_operacion2(n1, n2):
    return n1 - n2


def test_operacion3(n1, n2):
    return n1 * n2


def test_operacion4(n1, n2):
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


def test_mi_menu(argument, n1, n2):
    menu = {
        'suma': test_operacion1(n1, n2),
        'division': test_operacion4(n1, n2),
        'resta': test_operacion2(n1, n2),
        'multiplicacion': test_operacion3(n1, n2)
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
    test_mi_menu(operacion, num1, num2)
    print('seguir si o no?')
    opc = str(input())
    if opc == 'No' or opc == 'no' or opc == '0'or opc == 'N' or opc == 'n':
        bandera = False
    else:
        bandera = True
        tmp = sp.call('cls', shell=True)


