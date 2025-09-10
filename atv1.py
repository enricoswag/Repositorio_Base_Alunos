n1 = int(input("Digite um numero: "))

if n1 >= 0:
    if n1 % 2 == 0:
      quadrado = n1  ** 2
      print("o quadrado do numero {} é {}".format (n1, quadrado))
    else:
        cubo = n1 ** 3
        print(("O quadrado do numero {} é {}"))
else:
    print("Numero {} nao é positivo.".format(n1))