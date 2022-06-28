#Faça um Programa que leia um vetor A com 10 números inteiros,
# calcule e mostre a soma dos quadrados dos elementos do vetor.

vetorA = []
n = 0

for i in range(10):
    vetorA.append(int(input()))
    n += vetorA[i]**2

print(f'A soma dos quadrados é: {n}')
print(vetorA)