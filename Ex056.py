
mediaidade = 0
somaidade = 0
maioridade = 0
nomevelho = ""
countwomen = 0
for c in range(1,5):
    print('----{}ªPessoa----'.format(c))
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo[M/F]")).upper()
    somaidade += idade
    if c == 1 and sexo in "mM":
        maioridade = idade
        nomevelho = nome
    if sexo in "mM" and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        countwomen += 1

mediaidade = somaidade / 4
print ("A média da idade do grupo é de {} anos.".format(mediaidade))
if maioridade > 0:
    print ("O homem mais velho tem {} anos e seu nome é {}.".format(maioridade,nomevelho))
else:
    print("O grupo não contém nenhum homem.")
print ("O grupo contém {} mulheres menores de 20 anos.".format(countwomen))
