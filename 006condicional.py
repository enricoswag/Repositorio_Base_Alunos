# crie um codigo phyton que peça o valor da conta. se for maior que R$400,00
# adicione uma gorjeta de 10% e exiba o total pagar
# caso contrario, adicione uma gorjeta de 5%

# etapas para resoluçao
#1) solicitar o valor da conta de usuarip 
#2) se a conta for maior de 100 adicionar 10% de gorjeta e apresentar o total a pagar
#3) se a conta for menor que 100 adicionar 5% de gorjeta e apresentar o total a pagar

valor_da_conta = float(input("valor da conta r$: "))
if valor_da_conta >= 100: 
    valor_final =(valor_da_conta *0.1)
else:
    valor_final = valor_da_conta +(valor_da_conta*0.05)
    print(valor_final)