# Contar números pares e ímpares: O usuário digita vários números até informar 0. O programa
# deve mostrar quantos eram pares e quantos eram ímpares.

pares = 0
impares = 0

while True:
    numero = int(input("Digite um número (0 para encerrar): "))
    
    if numero == 0:
        break  
    
    if numero % 2 == 0:
        pares += 1  # Incrementa contador de pares
    else:
        impares += 1  # Incrementa contador de ímpares

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")

