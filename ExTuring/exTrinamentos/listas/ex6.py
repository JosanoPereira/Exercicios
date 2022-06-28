# Faça um Programa que peça as quatro notas de 10 alunos,
# calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

alunos = []
notas = []
listanotas = []
for i in range(1, 3):
    media = 0
    a = input('--Nome do Aluno: ')
    alunos.append(a)
    notas = []
    for j in range(1, 3):
        n = float(input('Nota do Aluno: '))
        notas.append(n)
        media += notas[j]


for x in range(len(alunos)):
    print(f'O aluno {alunos[x]} teve as segintes notas {notas}')
