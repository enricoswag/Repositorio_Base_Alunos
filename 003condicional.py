# Criar um codigo phyton fallando se a temperatura esta agradavel ou nao
# Condiçoes
# temperatura >= 30º informar que esta muito quente
# temperatura >= a 20º informar que a temperatura esta agradavel
# temperatura >= 10º informar que esta frio

# etapas para resoluçao:
#1) solicitar a temperatura ao usuario
#2) verificar a condicional
#3) imprimir a reposta segundo a temperatura

temperatura = float(input("DIGITE A TEMPERATURA DO DIAA:"))
if temperatura >= 30:
    print(f"a temperatura do dia é {temperatura}Cº e o dia esta muito quente")
elif temperatura >= 20:
     print(f"a temperatura do dia é {temperatura}Cº e o dia esta agradavel!!")
elif temperatura >= 10:
     print(f"a tempertura do dia é {temperatura}Cº e o dia esta frio")
else:
     print(f"a temperatura do dia é {temperatura}ºc e o dia esta frio demais") 