# Simulador de saque bancário: Peça ao usuário para digitar um valor para sacar. Enquanto ele
# tentar sacar um valor maior do que o saldo (ex.: saldo = 500), o programa deve avisar 'Saldo
# insuficiente'. Quando o saque for válido, mostrar 'Saque realizado' e encerrar.

saldo = 500.0  # Saldo inicial do usuário

while True:
    saque = float(input("Digite o valor que deseja sacar: R$ "))
    
    if saque > saldo:
        print("Saldo insuficiente! Tente um valor menor.")
    else:
        print("Saque realizado!")
        saldo -= saque
        print(f"Saldo restante: R$ {saldo:.2f}")
        break  # Encerra o loop após saque válido
