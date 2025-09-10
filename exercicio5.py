# 5)Cálculo de gorjeta
conta = float(input("Digite o valor da conta: R$ "))

if conta > 100:
    gorjeta = conta * 0.10
else:
    gorjeta = conta * 0.05

total = conta + gorjeta

print(f"Valor da conta: R$ {conta:.2f}")
print(f"Gorjeta a dar: R$ {gorjeta:.2f}")
print(f"Total a pagar: R$ {total:.2f}")