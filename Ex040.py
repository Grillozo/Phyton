# Aprovação Aluno

p1 = float(input("Nota da primeira prova: "))
p2 = float(input("Nota da segunda prova: "))
média = (p1 + p2) / 2
if média < 5:
    print("O aluno tirou {:.2F} na p1 e {:.2F} na p2, obteve uma média de {:.1F}, portanto está REPROVADO!".format(p1,p2,média))
elif média >= 5 and média < 7:
    print("O aluno tirou {:.2F} na p1 e {:.2F} na p2, obteve uma média de {:.1F}, portanto está de RECUPERAÇÃO!".format(p1,p2,média))
elif média >= 7:
    print("O aluno tirou {:.2F} na p1 e {:.2F} na p2, obteve uma média de {:.1F}, portanto está APROVADO!".format(p1,p2,média))
