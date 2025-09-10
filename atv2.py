usuario ="procopio"
senha = "12345"

usuario1= "paiva"
senha1= "54321"

login= input("Informe seu login: ").strip().lower()
senha_entrada= input("Informe sua senha: ").strip()

if (login == usuario and senha_entrada == senha) or (login == usuario1 and senha_entrada ==senha1):
    print("Seja bem-vindo!")
else:
    print("As senhas nao conferem.")