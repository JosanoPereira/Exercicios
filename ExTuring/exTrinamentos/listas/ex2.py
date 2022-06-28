# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

vetor = []
for i in range(1, 11):
    v = float(input())
    vetor.append(v)
print(vetor)
vetor.reverse()
print(vetor)