# calculadora
# 1 ingresar primer operando
# 2 ingresar segundo operando
# 3 elegir operacion -> sub menu con suma resta multiplicacion y division
# 4 mostrar resultado
# 5 salir
from funciones import *

numero_1 = None
numero_2 = None
que_es = None
rta = None

flag_numero = False
flag_numero2 = False
flag_operacion = False

while True:
    match menu_inicial(numero_1, numero_2, que_es, rta):
        case "1":
            numero_1 = pedir_numero()
            flag_numero = True
        case "2":
            if flag_numero:
                numero_2 = pedir_numero()
                flag_numero2 = True
            else:
                print("No ingresaste el primer numero")
        case "3":
            if flag_numero and flag_numero2:
                match menu_operaciones():
                    case "1":
                        rta = sumar(numero_1, numero_2)
                        que_es = "+"
                    case "2":
                        rta = restar(numero_1, numero_2)
                        que_es = "-"
                    case "3":
                        rta = multiplicar(numero_1, numero_2)
                        que_es = "*"
                    case "4":
                        rta = dividir(numero_1, numero_2)
                        que_es = "/"
                    case "5":
                        rta = factorial(numero_1)
                        que_es = "!"
                    case "6":
                        if confirmar("Esta seguro que desea salir? s/n: "):
                            break
                flag_operacion = True
            else:
                print("No ingreso ningun numero.")
        case "4":
            if flag_operacion:
                print(rta)
                numero_1 = None
                numero_2 = None
                que_es = None
                rta = None
                flag_numero = False
                flag_numero2 = False
                flag_operacion = False
            else:
                print("No ingreso ninguna operacion")
        case "5":
            if confirmar("Esta seguro que desea salir? s/n: "):
                break
    pausar()