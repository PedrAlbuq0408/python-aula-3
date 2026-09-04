def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero = indefinido"
    return a / b


num1 = float(input("Primeiro número: "))
num2 = float(input("Segundo número: "))


print("Divisão:", dividir(num1, num2))