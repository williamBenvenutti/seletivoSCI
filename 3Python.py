# 3 - Elabore um programa de computador que realize o cálculo de notas.
# Este programa deverá solicitar o nome do aluno e quatro notas, todo este conjunto deverá
# estar contido em um laço que confirme se deseja encerrar o programa ou continuar 
# solicitando outros nomes e notas.
# Ao final da solicitação do nome e das notas deverá ser impresso o nome do aluno e 
# a sua média, se a nota for  menor que 6 imprimir Reprovado, 
# senão, se a nota for igual ou maior que 6, imprimir Aprovado.


while True:
    print("Para finalizar, digite fim")
    nomeAluno = input("Digite o nome do Aluno: ")
    if nomeAluno.lower() == "fim":
        break

    notasAluno = []
    for i in range(4):
        notaDigitada = float(input("Digite a {}ª Nota:".format(i+1)))
        while (notaDigitada > 10 or notaDigitada < 0):
            print("Número fora do padrão!")
            notaDigitada = float(input("Digite a {}ª Nota:".format(i + 1)))
        notasAluno.append(notaDigitada)

    mediaAluno = sum(notasAluno)/len(notasAluno)

    print("Nome do Aluno: {}".format(nomeAluno))
    print("Media do Aluno: {}".format(mediaAluno))

    if (mediaAluno < 6):
        print("Aluno Reprovado!")
    else:
        print("Aluno Aprovado!")