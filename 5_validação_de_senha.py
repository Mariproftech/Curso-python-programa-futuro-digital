# Validação de senha: O programa deve pedir a senha (ex.: '1234') até que o usuário acerte.
# Quando acertar, mostrar 'Acesso permitido'

senha_correta = "1234"  
senha_digitada = ""     

while senha_digitada != senha_correta:
    senha_digitada = input("Digite a senha: ")
    if senha_digitada != senha_correta:
        print("Senha incorreta, tente novamente.")

print("Acesso permitido")
