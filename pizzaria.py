# crie um codigo phyton, utilizando match case
# que solicite ao usuario o tipo de pizza desejada e informe o preço

print("Menu pizzaria")
print("1- Margherita R$ 50,00")
print("2- Frango com catupiry 60.00")
print("3- quatro de queijos R$ 65.00")
print("4- portuguesa R$ 60,50")
print("5- Calabresa R$ 50,00")

tipo = int(input("digite um numero da pizza de 1 a 5: "))
match tipo:
    case 1:
        print("Margherita R$ 50,00")
    case 2:
        print("Frango com catupiry 60.00")
    case 3:
        print("quatro de queijos R$ 65.00")
    case 4:
        print("portuguesa R$ 60,5")
    case 5:
        print("5- Calabresa R$ 50,00")