# Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

vetor = []
vetorPar = []
vetorImpar = []
cont = 1
while cont <= 20:
    valor = int(input())
    if valor in vetor:
        print('Já esta no vector, insira outro')
        vetor.append(valor)
        vetor.pop()
    else:
        vetor.append(valor)
        if valor % 2 == 0:
            vetorPar.append(valor)
        else:
            vetorImpar.append(valor)
        cont+=1

print(vetor)
print(vetorPar)
print(vetorImpar)