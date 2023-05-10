"""Missing module docstrings"""

decrescente = True
anterior = int(input("DIGITE O PRIMEIRO NÚMERO: "))
valor = 1

while valor != 0 and decrescente:
    valor = int(input("DIGITE O PRÓXIMO NÚMERO: "))
    if valor > anterior:
        decrescente = False
    anterior = valor
    
if decrescente == True:
    print("A SEQUÊNCIA ESTÁ EM ORDEM DECRESCENTE!!! ")
else:
    print("A SEQUÊNCIA NÃO ESTÁ EM ORDEM DECRESCENTE!!! ")