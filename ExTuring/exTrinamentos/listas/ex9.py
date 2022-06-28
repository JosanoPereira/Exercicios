#Faça um Programa que leia dois vetores com 10 elementos cada.
# Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

lista1 = []
lista2 = []
lista = []

for i in range(10):
    lista1.append(input('Insira o valor na lista 1: '))

for j in range(10):
    lista2.append(input('Insira o valor na lista 2: '))

for k in range(len(lista2)):
    lista.append(lista1[k])
    lista.append(lista2[k])

print(lista1)
print(lista2)
print(lista)