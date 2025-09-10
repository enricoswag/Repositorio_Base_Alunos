# Crie um codigo phyton que solicite ao usuario o codigo de um
# produto e informe o preço

print("menu de produtos")
print("1-Café")
print("2- chá")
print("3- suco")
print("4-Refrigente")
print("5- àgua")

codigo = int(input("Digite o codigo do produto: "))

match codigo:
    case 1:
        print("Produto café 500g: R$ 36,00")
    case 2:
        print("Produto chá 100g: R$ 8,00")
    case 3:
        print("Produto suco 1l: R$ 16,00")
    case 4:
        print("Produto Refrigerante 2l: R$ 18,00")
    case 5:
        print("Produto: Àgua 500 ml: R$ 12,00")
    case _:
        print("Digite um codigo valido.")