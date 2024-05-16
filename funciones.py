def menu_inicial(a: any, b: any, c: any, d: any)-> str:
    """un menu diseñado para una calculadora

    Args:
        a (_type_): el primer operando
        b (_type_): el segundo operando
        c (_type_): la operacion
        d (_type_): el resultado

    Returns:
        str: la opcion elegida
    """
    limpiar_pantalla()
    print("------------------------------------------")
    print(f"{'calculadora':^50s}")
    print(f"1- primer operando (x = {a})")
    print(f"2- segundo operando (y = {b})")
    print(f"3- elegir operacion ({a } {c} {b})")
    print(f"4- mostrar resultado ({d})")
    print("5- salir")
    return input("ingrese opcion: ")

def menu_operaciones()-> str:
    """un menu con operaciones para usar en una calculadora

    Returns:
        str: la opcion elegida
    """
    limpiar_pantalla()
    print("------------------------------------------")
    print(f"{'operaciones':^50s}")
    print("1- suma")
    print("2- resta")
    print("3- multiplicacion")
    print("4- division")
    print("5- factorial")
    print("6- salir")
    return input("ingrese opcion: ")

def sumar(a: int, b: int)-> int:
    """hace una suma de dos enteros

    Args:
        a (int): primer numero a sumar
        b (int): segundo numero a sumar

    Returns:
        int: la suma realizada
    """
    return a + b

def restar(a: int, b: int)-> int:
    """hace la resta de dos enteros

    Args:
        a (int): primer numero a restar
        b (int): segundo numero a restar

    Returns:
        int: la resta realizada
    """
    return a - b

def multiplicar(a: int, b: int)-> int:
    """hace la multiplicacion de dos enteros

    Args:
        a (int): primer numero a multiplicar
        b (int): segundo numero a multiplicar

    Returns:
        int: la multiplicacion realizada
    """
    return a * b


def dividir(a: int, b: int)-> float:
    """hace la division de dos enteros

    Args:
        a (int): primer numero a dividir
        b (int): segundo numero a dividir

    Returns:
        float: la division realizada
    """
    return a / b

def factorial(n: int)->int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def pedir_numero()-> int:
    """pide un numero y lo retorna

    Returns:
        int: numero ingresado
    """
    numero = int(input("Ingrese un numero: "))
    return numero

def confirmar(mensaje:str)-> bool:
    """confirma con un booleano

    Args:
        mensaje (str): pregunta que sera respondida por el usuario

    Returns:
        bool: True si la respuesta es si, False si es no
    """
    rta = input(mensaje).lower()
    return rta == 's'

def pausar():
    """pausa el programa
    """
    import os
    os.system("pause")

def limpiar_pantalla():
    """limpia la pantalla
    """
    import os
    os.system("cls")