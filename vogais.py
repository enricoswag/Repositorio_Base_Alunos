# Peça ao usuario para digitar uma letra
# se for vogal informe qual
# se for consoante , verifique se é maiuscula ou minusculo
# selecione de entrada do tipo string (texto)
letra = input("digite uma letra: ")

if letra.lower() in "aeiou": # .lower() transforma para minusculo 
    print(f'Vogal: {letra}')
else:
    if letra.isupper(): # issuper identifica se a letra esta em maiusculo
        print(f"Consoamte minuscula: {letra}")
    else:
        print(f"Comsoante minuscula: {letra}")