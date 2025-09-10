salario = float(input("informe seu salario mensal: "))
cargo = input("Por favor, informe seu cargo: ")

programador = 10000
analista_sistema = 7000
analista_dados = 12000

if cargo == "programador":
    salario_novo = salario * 1.30
    print("O novo salario do programador é R${} ".format(salario_novo))
elif cargo == "analista_de_dados":
    salario_novo = salario * 1.20
    print("O novo salario do analista de dados é R$ {}.".format(salario_novo))
elif cargo == "analista de sistemas":
    salario_novo = salario * 1.15
    print("O novo salario de analista de dados é R$ {}.".format(salario_novo))
else:
    print("Cargo nao foi encontrado.")