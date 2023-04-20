def calculadora(num1, num2, operacion):
    try:
        if operacion == '+':
            resultado = num1 + num2
        elif operacion == '-':
            resultado = num1 - num2
        elif operacion == '*':
            resultado = num1 * num2
        elif operacion == '/':
            resultado = num1 / num2
        else:
            return "Operación no válida"
    except ZeroDivisionError:
        return "Error: no se puede dividir por cero"
    
    return resultado