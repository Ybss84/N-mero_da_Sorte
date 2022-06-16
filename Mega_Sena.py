import random

mega_sena = random.sample(range(0, 60), 6)
quina1 = random.sample(range(0, 80), 5)
quina2 = random.sample(range(0, 80), 15)
loto_facil = random.sample(range(0, 25), 15)

name = str(input("Informe o seu nome: "))
print(f"\nObrigado pela confirmação {name}")
print("\n")
print("\n")
print(f"\n{name}, temos essas opções para criar apostas: ")
print(f"\n1- Mega Sena")
print(f"\n2- Quina")
print(f"\n3- Loto-Fácil")
res = int(input("\nInforme a opção desejada: "))

if res == 1:
    print(f"\n{name}, os números para jogar na mega-sena é: {mega_sena}")

elif res == 2:
    
    print(f"\n{name}, para essa opção temos dois tipos de jogo. ")
    print("\n1- Para aposta com 5 números na quina")
    print("\n2- Para aposta com 15 números na quina")
    res2 = int(input("\nInforme a opção desejada: "))

    if res2 == 1:
        print(f"\nOpção escolhida foi 1: {quina1}")
    
    elif res2 == 2:
        print(f"\nOpção escolhida foi 2: {quina2}")
    
    else:
        print("Erro!")

elif res == 3:
    print(f"\n{name}, os números para jogar na Loto-Fácil é: {loto_facil}")

else:
    print("Erro!")