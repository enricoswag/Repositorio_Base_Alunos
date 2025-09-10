# 2. paridade e tamanho do numero

# crie um codigo que receba um numero inteiro e informe:
# - se par ou impar
# - e,ao mesmo tempo, se é maior que 10 ou menor ou =
# Utilize concidencias aninhadas para organizar as verificaçoes


num = int(input("Digite um número inteiro: "))
if num % 2 == 0:
    print("O número é par.")
    if num > 10:
        print("E também é maiior que 10.")
    elif num== 10:
        print("E também é igual a 10.")
    else:
        print("E também é maior que 10.")
else:
    print("O número é impar.")
    if num > 10:
        print("E também é maior que 10.")
    elif num == 10:
        print("E também é igual a 10.")
    else:
        print("E também é menor que 10.")