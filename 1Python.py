# 1 - Solicitar a inserção de 5 números, ao final, imprimir os números pares,
# números impares e a média geral desses números.

numerosDigitados = []
numerosPares = []
numerosImpares = []

for i in range(5):
    numeroDigitado = int(input("Digite um número: "))
    numerosDigitados.append(numeroDigitado)
    if numeroDigitado % 2 == 0:
        numerosPares.append(numeroDigitado)
    else:
        numerosImpares.append(numeroDigitado)

mediaNumeros = sum(numerosDigitados)/len(numerosDigitados)

print("Números pares {}".format(numerosPares))
print("Números impares {}".format(numerosImpares))
print("Média dos numeros Digitados {}".format(mediaNumeros))