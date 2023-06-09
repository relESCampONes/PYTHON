import random
import sys

sortear = []
sorteados = []
acertados = []
acertos = 0

sortear.append(int(input("DIGITE O PRIMEIRO NÚMERO: ")))
sortear.append(int(input("DIGITE O SEGUNDO NÚMERO: ")))
sortear.append(int(input("DIGITE O TERCEIRO NÚMERO: ")))
sortear.append(int(input("DIGITE O QUARTO NÚMERO: ")))
sortear.append(int(input("DIGITE O QUINTO NÚMERO: ")))
sortear.append(int(input("DIGITE O SEXTO NÚMERO: ")))

for i in sortear:
    if i < 1 or i > 60:
        print("É NECESSÁRIO DIGITAR UM NÚMERO ENTRE 1 E 60, FAÇA UM PRÓXIMO JOGO!!!")
        sys.exit()



def mega_sena(a):
    while a in (sorteados):
        a = random.randint(1,60)
    return a

sorteados.append(random.randint(1,60))
sorteados.append(mega_sena(random.randint(1,60)))
sorteados.append(mega_sena(random.randint(1,60)))
sorteados.append(mega_sena(random.randint(1,60)))
sorteados.append(mega_sena(random.randint(1,60)))
sorteados.append(mega_sena(random.randint(1,60)))

sorteados_resultado = sorted(sorteados)
sortear_conferir = sorted(sortear)

print("\nO SORTEIO DA MEGA SENA FOI FEITO\n------------------------------------------------------------------\nOS NÚMEROS DA MEGA SENA SÃO:\n")

for i in sorteados_resultado:
    print(f"{i:02} | ", end="")

print("\n\nOS SEUS NÚMEROS SÃO:\n")

for i in sortear_conferir:
    print(f"{i:02} | ", end="")


# print("\n")

for i in range(0,5):
    if sortear[i] in (sorteados):
        acertados.append(sortear[i])

acertos = len(acertados)

if acertos <= 1:
    print("\n\nNÚMEROS ACERTADOS: ",sorted(acertados))
    print(f"ACERTOU: {acertos} DEZENA, TENTE UMA PRÓXIMA VEZ!!!")
elif acertos <= 3:
    print("\n\nNÚMEROS ACERTADOS: ",sorted(acertados))
    print(f"ACERTOU: {acertos} DEZENAS, TENTE UMA PRÓXIMA VEZ!!!")
elif acertos == 4:
    print("\n\nNÚMEROS ACERTADOS: ",sorted(acertados))
    print("PARABÉNS, ACERTOU A QUADRA E RECEBERÁ UM PRÊMIO!!!")
elif acertos == 5:
    print("\n\nNÚMEROS ACERTADOS: ",sorted(acertados))
    print("SURPREENDENTE, ACERTOU A QUINA E RECEBERÁ UM ÓTIMO PRÊMIO!!!")
else:
    print("\n\nNÚMEROS ACERTADOS: ",sorted(acertados))
    print("---GLÓRIA A DEUS, GANHOU NA MEGA SENA, ACERTOU OS 6 NÚMEROS E VAI LEVAR TUDO!!!!!!---")




# def random_exclude(range_start, range_end, excludes):
#     r = random.randint(range_start, range_end)
#     if r in excludes:
#         return random_exclude(range_start, range_end, excludes)
#     return r

# or

# def random_exclude(range_start, range_end, excludes):
#     r = random.randint(range_start, range_end)
#     while r in excludes:
#         r = random.randint(range_start, range_end)
#     return r
