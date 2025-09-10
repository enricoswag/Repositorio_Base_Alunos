nome = input("Diga seu nome: ")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite quantos metros você tem: "))

imc = peso / (altura ** 2)

if imc >= 40.0:
    print(f"Muito cuidado {nome} com sua saude, seu imc é {imc}! você possui obesidade grau 3.")
elif 35.0 <= imc <= 39.9:
    print(f"Seu imc é {imc} e você possui obesidade grau 2, cuidado {nome}.")
elif 30.0 <= imc <= 34.9:
    print(f"Seu imc é {imc} e você possui obesidade grau 1, cuidado {nome}!")
elif 25.0 <= imc < 29.9:
    print(f"Você está sobrepeso Seu imc é {imc}, cuidado {nome}!")
elif 18.5 <= imc < 24.9:
    print(f"Parabéns Seu imc é {imc}, seu imc está normal {nome}.")
if imc < 18.5:
    print(f"Cuidado! Seu imc é {imc}, Você está abaixo do peso {nome}.")