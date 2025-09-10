valor_venda = float(input("Informe o valor total: "))
forma_pagamento = input("informe a forma de pagamento")
print("Tabela de Formas de Pagamento")
print("1- À vista (em espécie) ")
print("2- Cartão de débito")
print("3- Cartão de crédito (vencimento)")

valor_venda = float(input("Informe o valor total da venda R$: "))
forma_pagamanto = input("Informe a forma de pagamento (1|2|3): ")

if forma_pagamanto == "1":
    valor_final = valor_venda * 0.85
    print("Obrigada pela sua compra, você recebeu um desconto e o valor final é R${}".format(valor_final))
elif forma_pagamanto == "2":
    valor_final = valor_venda * 0.90
    print("Obrigada pela sua compra, você recebeu um desconto e o valor final é R${}".format(valor_final))
elif forma_pagamanto == "3":
    valor_final = valor_venda * 0.95
    print("Obrigada pela sua compra, você recebeu um desconto e o valor final é R${}".format(valor_final))
else:
    print("Digite uma opção de pagamento válida.")
