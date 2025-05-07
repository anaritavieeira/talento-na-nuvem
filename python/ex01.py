while True:
    andar = int(input("escolha um número de andar entre 1 e 20: "))
    
    if andar == 13:
        print("desculpe, não temos o 13º andar. tente novamente!")
        continue
    
    if 1 <= andar <= 20:
        print(f"o andar escolhido foi: {andar}")
        break
    else:
        print("número de andar inválido! tente novamente.")