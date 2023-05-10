import sys
carro = "çççççpeéébé"
barro = "é"
sys.stdout.buffer.write(carro.encode('utf-8'))
sys.stdout.buffer.write(barro.encode('utf-8'))
