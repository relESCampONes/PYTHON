# Fibonacci
a, b, c = 0, 1, 0
term = int(input("Which fibonacci term do you want to know? "))
while c < term-1 :
    # print(b)
    a, b = b, a + b
    c = c + 1
print(b)
