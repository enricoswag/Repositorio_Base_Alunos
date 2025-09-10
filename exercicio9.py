# 9)Desconto em compras por valor mínimo

compra = float(input("Digite o valor da compra: R$ "))

if compra > 150:
    desconto = 20
else:
    desconto = 5

total = compra - desconto

print(f"Valor da compra: R$ {compra:.2f}")
print(f"Desconto aplicado: R$ {desconto:.2f}")
print(f"Total a pagar: R$ {total:.2f}")