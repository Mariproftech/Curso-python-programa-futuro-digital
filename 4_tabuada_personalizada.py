# Tabuada personalizada: Peça para o usuário digitar um número. O programa deve mostrar a
# tabuada desse número (1 a 10) usando `while`.

numero = int(input("Digite um número para ver sua tabuada: "))

contador = 1  # Começa no 1

while contador <= 10:  # Enquanto o contador for de 1 a 10
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador += 1  # Incrementa o contador
