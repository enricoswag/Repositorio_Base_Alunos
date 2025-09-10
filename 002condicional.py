# Crie um codigo que receba 3 notas, calucle a media
#e informe se o aluno esta aprovado ou em recuperação
# ou reprovado

# OBS: aprovado, media >=7
# recuperação media > 4
# reprovado media < 4

# Etapas 
# 1) solicitar as notas de um usuario
n1 = float(input(" Digite a primeira nota: "))
n2 = float(input(" Digite a segunda nota: "))
n3 = float(input(" Digite a terceira nota: "))
# 2) calcular as média
media = (n1 + n2 + n3)/3

# 3) checar a condiçao do aluno

# 4) informar o resultado 
if media>=7:
        print(f"O aluno tem media {media: .2f} e esta aprovado")
elif 5 <= media < 7:
        print(f"O aluno tem media {media: .2f} e esta em recuperacao")
else:
        print(f"O aluno tem media {media: .2f} e esta reprovado")