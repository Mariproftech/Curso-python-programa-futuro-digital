# Somatório até zero: O usuário deve digitar números. O programa deve somar todos eles até
 # que o usuário digite 0. No final, mostre a soma total.

soma = 0  

while True:
    numero = float(input("Digite um número (0 para encerrar): "))
    if numero == 0:
        break  
    soma += numero  

print(f"A soma total dos números é: {soma}")
