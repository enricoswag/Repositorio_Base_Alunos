apresentador = input("informe o sobrenome  do seu apresentador favorito: ").strip().lower()

if apresentador == "pinheiro" or apresentador == "araujo":
    print("esses sao os apresentadores do Bom Dia nação.")
elif apresentador == "bonner" or apresentador == "vasconcelos":
    print("Esse é um(a) apresentador do jornal brasileiro")
else:
    print("Apresentador desconhecido")