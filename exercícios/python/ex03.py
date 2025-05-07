def calculadora():
    while True:
        print("escolha uma operação:")
        print("1- somar")
        print("2- subtrair")
        print("3- multiplicar")
        print("4- dividir")
        print("0- sair")

        try:
            opcao = int(input("digite o número para a operação que deseja: "))
        except ValueError:
            print("por favor, insira uma opção válida")
            continue

        if opcao == 0:
            print("saindo do programa...")
            break

        if opcao not in [1, 2, 3, 4]:
            print("essa opção não é válida")
            continue

        try:
            num1 = float(input("digite o primeiro número: "))
            num2 = float(input("digite o segundo número: "))
        except ValueError:
            print("por favor, insira números válidos")
            continue

        if opcao == 1:
            resultado = num1 + num2
            print(f"o resultado da soma é: {resultado}")
        elif opcao == 2:
            resultado = num1 - num2
            print(f"o resultado da subtração é: {resultado}")
        elif opcao == 3:
            resultado = num1 * num2
            print(f"o resultado da multiplicação é: {resultado}")
        elif opcao == 4:
            if num2 == 0:
                print("divisão por zero não é válida")
            else:
                resultado = num1 / num2
                print(f"o resultado da divisão é: {resultado}")

        print()

calculadora()
