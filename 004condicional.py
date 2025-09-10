# crie um codigo em phyton que peça um numero a um usuario
# e exiba "NUMERO PAR" se ele for divisivel por 1

# etapas de resolução:

#1) solicitar um numero ao usuario
#2) verificar se o numero e par ou impar
#3) informar se o numero e par ou impar

numero = float(input("digite seu numero: "))

if numero % 2 == 0:
    print(f"o numero {numero} é par.")
else:
    print(f"o numero {numero} é impar.")