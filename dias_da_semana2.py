dia = int(input("digite um numero de 1 a 7: "))

match dia:
    case 1|2|3|4|5|6:
        print("Ainda não é final de semana. Força !")
    case 1|7:
        print("Oba! chegou o fds!!")
    case _:
        print("numero invalido. Digite um numero de 1 a 7: ")
