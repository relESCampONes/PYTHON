# Arredondamento e f-Strings
print(8/3)
# Retorna ponto flutuante 2.66666666
print(round(8/3))
# Vai ser impresso 3, pois essa divisão resulta 2.6 e round arredonda e logo se torna 3
print(round(8/3, 2))
# É possível inserir após a vírgula, quantas casas decimais de arredondamento deseja resultando 2.67
print(round(2.666666, 2))
# Também resultará em 2.67
print(8//3)
# Retorna apenas o número inteiro 2


score = 0
score += 4
height = 1.8
isWinning = True
points = 17
carro = 23
print(f"Pontuei {score}, porque tenho {height}m de altura, será què ^^ não ganhei? {isWinning}")
