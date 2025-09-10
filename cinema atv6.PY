# Exemplo: Verificador de idade para cinema
idade = int(input("Digite sua idade: "))
if idade < 12:
    print("🎬 Filmes liberados: Livre")
elif idade < 14:
    print("🎬 Filmes liberados: Livre e 10 anos")
elif idade < 16:
    print("🎬 Filmes liberados: Livre, 10 e 12 anos")
elif idade < 18:
    print("🎬 Filmes liberados: Livre, 10, 12 e 14 anos")
else:
    print("🎬 Todos os filmes liberados! 🍿")