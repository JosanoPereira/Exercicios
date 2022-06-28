# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

con = []
cont = 1
nc = 0
while cont <= 10:
    c = input()
    con.append(c)
    cont += 1
print(con)
for i in con:
    if i in 'bcdfghjklmnpqrstvwxyz':
        nc += 1
print(nc)