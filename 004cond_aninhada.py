# tipo de triangulo
# crie um programa que receba tres lados de um triangulo
# verifique se os lados realmente podem formar um triangulo
# e determine os triangulos em:
# equilatero (todos os lados iguais)
# isoceles (dois lados iguais)
# Escaleno (todos os lados diferentes)
a = int(input("Digite o valor do lado a: "))
b =  int(input("Digite o valor do lado b: "))
c =  int(input("Digite o valor do lado c: "))

# Verifique se o lados formam um triangulo
if a + b > c and a + c > b and b + c > a: # condiçao para a formaçao do triangulo
       print(f"os lados do triangulo são {a}, {b} e {c}: triangulo isoceles")
else: # nao é possivel formar triangulo
      if b or a == c:
        print(f"os lados do triangulo são {a}, {b} e {c} triangulo isoceles")
      else:
        print("Os lados nao formam um tringulo valido")