# 3. classificar por idade
# 3. faça um programa que leia a idade de uma pessoa e classifique-a em:
# criança: menor que 12 anos
# adolescente: entre 12 e 17 anos.
# adulto maior ou igual a 18 anos
# utilize a estrutura condicional aninhada

idade = int(input("digite sua idade"))
if idade >=0:
    if idade >= 18:
        print(f"Voce tem {idade} anos e é adulto")
    elif 12 <=idade <=17:
        print(f"Voce tem {idade} anos e é adolescente")
else:
    print("Idade nao pode ser negativa, digite uma idade valida.")