# objetivo: calcular a idade do usuário a partir do ano do seu nascimento e do ano atual;

nome = input("digite o seu nome: ")

while True:
    try:
        ano = int(input("digite o ano do seu nascimento (entre 1922 e 2024): "))
        if ano >= 1922 and ano <= 2024:
            break
        else:
            print("ano fora do intervalo permitido")
    except:
        print("entrada inválida. por favor, digite um número")

ano_atual = 2025
idade = ano_atual - ano
print(f"{nome}, você vai ter {idade} anos em {ano_atual}.")
