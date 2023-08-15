# Lectura del valor de 2 variables enteras por consola:
print("Ingrese el número 1")
número1 = int(input())
print("Ingrese el número 2")
número2 = int(input())
print("Ingrese la operación (+, -, *, /, %, **)")
operación = input()

match operación:
    case '+':
        # Operación suma:
        suma = número1 + número2
        print("La suma es " + str(suma))
    case '-':
        # Operación resta:
        resta = número1 - número2
        print("La resta es " + str(resta))
    case '*':
        # Operación multiplicación:
        multiplicacion = número1 * número2
        print("La multiplicación es " + str(multiplicación))
    case '/':
        # Operación división:
        division = número1 / número2
        print("La división es " + str(division))
    case '%':
        # Operación módulo:
        módulo = número1 % número2
        print("El residuo de la división es " + str(módulo))
    case '**':
        # operación potencia:
        potencia = número1 ** número2
        print("La potencia del número es " + str(potencia))
    case print("Operación inválida")