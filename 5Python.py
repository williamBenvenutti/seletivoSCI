# 5 - Crie uma matriz bidimensional. Deverá ser solicitado três nomes de alunos e quatro notas, 
# após solicitação dos nomes e das notas deverá ser impresso os nomes acompanhados da média 
# geral de cada aluno, deverá ser impresso também o nome do aluno que obteve a maior média e o 
# nome do aluno que obteve a menor média.

matrizNotas = []
menorMedia = 11
maiorMedia = -1
alunoMenor = ""
alunoMaior = ""

for i in range(3):
    nomeAluno = input("Digite o nome do {}º Aluno: ".format(i+1))
    notasAlunos = []
    for j in range(4):
        notaDigitada = float(input("Digite a {}ª Nota: ".format(j+1)))
        notasAlunos.append(notaDigitada)
    matrizNotas.append([nomeAluno, notasAlunos])

for alunoBase in matrizNotas:
    nomeAluno = alunoBase[0]
    notasAlunos = alunoBase[1]
    mediaAluno = sum(notasAlunos) / len(notasAlunos)

    if mediaAluno > maiorMedia:
        maiorMedia = mediaAluno
        alunoMaior = nomeAluno

    if mediaAluno < menorMedia:
        menorMedia = mediaAluno
        alunoMenor = nomeAluno

    print("-"*30)
    print("Nome do Aluno: {} | Média do Aluno: {}".format(nomeAluno, mediaAluno))
    print("-"*30)

print("Maior média -- Nome do Aluno: {} | Média do Aluno: {}".format(alunoMaior, maiorMedia))
print("-"*30)
print("Menor média -- Nome do Aluno: {} | Média do Aluno: {}".format(alunoMenor, menorMedia))