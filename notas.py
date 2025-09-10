# Crie um código python, utilizando match case que analise as notas dos alunos:
# 1) Peça ao usuário 4 notas
# 2) calcule a média
# 3) classifique a média em:
# 0 a 4 = reprovado
# 5 e 6 = recuperação
# 7 a 10 = aprovado

print("0 a 4 reprovado")
print("5 a 6 recuperação")
print("7 a 10")

nota = float(input("digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))
nota4 = float(input("Digite sua quarta nota: "))

media = (nota + nota2 + nota3 + nota4)/4

match media:
    case 7|8|9|10:
        print("Aprovado. voce passou")
    case 1|2|3|4:
        print("Você esta reprovado. adeus.")
    case 5|6:
        print("Você esta de recuperação, ainda há chances.")
    case _:
        print("digite um numero valido.")