# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []
cont = 1
while cont <= 4:
    n = float(input())
    notas.append(n)
    cont+=1
media = sum(notas)/len(notas)
print(notas)
print(media)