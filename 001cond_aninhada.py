num = int(input("Digite um numero inetrio: "))

if num >= 0:
    if num == 0:
        print("o numero digitado é 0 ")
    else:
        print(f"o numero {num} é positivo.")
else:
    print(f"o numero {num} é negativo.")