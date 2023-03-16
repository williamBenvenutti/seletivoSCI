# 2 - Solicitar 5 números, ao fim, imprimir o número maior e o número menor.

numerosDigitados = []

for i in range(5):
    numeroDigitado = int(input("Digite um número: "))
    numerosDigitados.append(numeroDigitado)
    
maiorNumero = max(numerosDigitados)
menorNumero = min(numerosDigitados)

print("O maior número é: {}".format(maiorNumero))
print("O menor número é: {}".format(menorNumero))
