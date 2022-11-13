import random

user_points = 0
computer_points = 0

while True:
    user_choice = input("Escolha (R)Pedra, (P)Papel ou (T)Tesoura. Para sair pressione o Q.").lower()

    if user_choice == 'q':
        break
    
    computer_choice = random.randint(0, 2)

print("GoodBye!")