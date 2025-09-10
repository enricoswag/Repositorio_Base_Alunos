# crie um codigo phyton que verifique a senha digitada 
# pelo usuario (se for) "1234", "exiba acesso permitido."

# etapas para resoluçao
# criar uyma variavel e a atribuir uma senha
# atraves de um input solicitar a senha ao usuario 
# liberar ou nao o acesso ao usuario 
# ATRAVES da condicional checar se a senha e igual a armazenada

senha = "scrt"

senha2 = input("digite sua senha: ")

if senha2 == senha:
    print("Acessado com successo")
else:
    print("acesso negado. tente denovo.")