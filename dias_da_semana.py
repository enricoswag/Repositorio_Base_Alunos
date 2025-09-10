# crie um programa que:
#1) Peça ao usuario que difite um numero de 1 a 7 para indicar
#os dias da semana
# Use match case para exibir o nome correspondente ao numero
# 1-Domingo
# 2-segunda-feira
# 3-terça-feira
# 4-quarta-feira
# 5-quinta-feira
# 6- sexta-feira
# 7-sabado

dia = int(input("digite um numero de 1 a 7: "))

match dia:
    case 1: 
       print("Hoje é domingo.Boa semana")
    case 2:
        print("Hoje é segunda-feira.Boa semana")
    case 3:
        print("Hoje é terça-feira.Boa semana")
    case 4:
        print("Hoje é quarta-feira.Boa semana")
    case 5:
        print("Hoje é quinta-feira.Boa semana")
    case 6:
        print("Hoje é sexta. sextou!!!!!!!!!!!")
    case 7:
        print("Hoje é sabado.")