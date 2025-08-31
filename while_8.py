# Média de notas: O usuário digita notas de alunos. O programa continua pedindo notas até que
# o usuário digite -1. No final, mostra a média das notas digitadas.

soma = 0        
quantidade = 0  

while True:
    nota = float(input("Digite a nota do aluno (-1 para encerrar): "))
    
    if nota == -1:
        break  
    
    soma += nota
    quantidade += 1

# Calcula a média, se houver pelo menos uma nota
if quantidade > 0:
    media = soma / quantidade
    print(f"A média das notas digitadas é: {media:.2f}")
else:
    print("Nenhuma nota foi digitada.")
