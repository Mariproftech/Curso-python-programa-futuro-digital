# Caixa registradora simples: Peça preços de produtos até que o usuário digite 0. No final,
# mostre o total da compra.

total = 0.0  # Acumula o total da compra

while True:
    preco = float(input("Digite o preço do produto (0 para encerrar): "))
    
    if preco == 0:
        break  
    
    total += preco  

print(f"Total da compra: R$ {total:.2f}")
