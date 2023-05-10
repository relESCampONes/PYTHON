# Day 1
print("Hello World!!!")
print("Hello"+"World!!!")
print("Hello"+" "+"World!!!")
print("Hello" " " + "World!!!")
print("Hello "+input("What's your name?\n"))
nome = input("What's your name?\n")
lett = len(nome)
print("Hello {nome}, your name has {lett} letters")

#Entrar com duas variáveis e invertelas
a = int(input("a: "))
b = int(input("b: "))


#Solução é criar uma terceira variável e substuir pela primeira

c = a
a = b
b = c

print(f"a: {a}")
print(f"ab: {b}")
