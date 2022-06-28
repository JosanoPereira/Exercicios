#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
# Imprima a idade e a altura na ordem inversa a ordem lida.

idade = []
altura = []

for i in range(1, 6):
    idade.append(int(input(f'Insira a {i}° idade: ')))
    altura.append(float(input(f'Insira a {i}° altura: ')))

idade.reverse()
altura.reverse()
print(idade)
print(altura)