def calculadora(num1, num2, operacao):
    if operacao == 1:
        resultado = num1 + num2
        return resultado
    elif operacao == 2:
        resultado = num1 - num2
        return resultado
    elif operacao == 3:
        resultado = num1 * num2
        return resultado
    elif operacao == 4:
        if num2 == 0:
            return "não é possível dividir por zero"
        resultado = num1 / num2
        return resultado
    else:
        return 0

try:
    num1 = float(input("digite o primeiro número: "))
    num2 = float(input("digite o segundo número: "))
    operacao = int(input("escolha a operação (1- soma, 2- subtração, 3- multiplicação, 4- divisão): "))

    resultado = calculadora(num1, num2, operacao)

    print(f"o resultado é: {resultado}")

except ValueError:
    print("por favor, insira valores válidos.")
