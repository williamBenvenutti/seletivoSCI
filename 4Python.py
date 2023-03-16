# 4 - Criar um vetor de cinco posições, solicitar 
# cinco números e ao fim, imprimir o valor apresentado na posição três.

numerosDigitados = []

for i in range(5):
    numeroDigitado = int(input("Digite um número: "))
    numerosDigitados.append(numeroDigitado)

print("Número na Posição 3 do vetor: {}".format(numerosDigitados[2]))