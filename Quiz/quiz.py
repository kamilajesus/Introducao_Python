print("Seja bem vindo ao quiz da Kamila!")
answer_user = input("Quer começar? (S/N)")

if answer_user != "S":
    quit()

score = 0

print("Começando...")

print("Quantos planetas cabem dentro do sol? \n (A) Um milhão \n (B) Cem \n (C) Seiscentos \n (D) Cento e cinquenta \n")
answer_1 = input("Resposta: ")

if answer_1 == "A":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print("Em que lugar vivem mais cangurus do que pessoas? \n (A) Nova Azelândia \n (B) Indonésia  \n (C) Austrália \n (D) Africa do Sul \n")
answer_2 = input("Resposta: ")

if answer_2 == "C":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print("Quanto mede uma girafa? \n (A) 2,5 metros \n (B) Entre 4,8 e 5,5 metros \n (C) 3 metros \n (D)  Entre 5 e 6 metros \n")
answer_3 = input("Resposta: ")

if answer_3 == "B":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print(" Quantos braços tem um polvo? \n (A) Seis \n (B) Sete \n (C) Dez \n (D) Oito \n")
answer_4 = input("Resposta: ")

if answer_4 == "D":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")


print("Quanto tempo o vidro demora para se decompor? \n (A) 100 anos \n (B) 4000 anos  \n (C) Tempo indetermidado \n (D) 1 milhão de anos  \n")
answer_5 = input("Resposta: ")

if answer_5 == "C":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print(f"Quiz acabou... Pontuação: {score}/5")