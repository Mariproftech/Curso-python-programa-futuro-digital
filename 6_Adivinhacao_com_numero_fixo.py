# Adivinhação de número secreto: O computador escolhe um número (fixo ou aleatório). O
# usuário deve tentar adivinhar. Enquanto ele errar, o programa continua pedindo. Quando
# acertar, mostrar 'Parabéns, você acertou!'.

numero_secreto = 7  
palpite = None      

while palpite != numero_secreto:
    palpite = int(input("Tente adivinhar o número (entre 1 e 10): "))
    if palpite != numero_secreto:
        print("Errado! Tente novamente.")

print("Parabéns, você acertou!")
