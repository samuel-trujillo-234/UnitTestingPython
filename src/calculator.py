def sum(a, b):
    return a + b 

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("La division por cero no esta permitida")
    return a / b



