# print("Olá amigos")

import statistics as es

historia_n1 = float(input("Digite sua primeira nota: "))
historia_n2 = float(input("Digite sua segunda nota: "))

# Jeito 1

# soma = historia_n1 + historia_n2
# media = soma/2
# print("sua média é: " + str(media))

# Jeito 2 

listas_notas = [historia_n1, historia_n2]
media = es.mean(listas_notas)
print("sua média é: " + str(media))

# Se
if media >= 7:
    print("APROVADISSIMOOOOOOOO")

# Se não, se
elif media >=5 and media < 7:
    print("OPS!! CHAMA NA RECUPERAÇÃO")

# caso contrário
else:
    print("VOOOOCÊ FOI REPROVADOOOOOO")
