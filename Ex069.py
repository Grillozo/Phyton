
contp = contfem = contmasc = contfem20 = 0

while True:
    i = int(input("Idade: "))
    s = " "
    while s not in "mMFf":
        s = str(input("Sexo[M/F]: ")).strip()[0].lower()
        if s in "m":
            contmasc += 1
        if s in "f":
            contfem += 1
        if s == "f" and i < 20:
            contfem20 += 1
        contp += 1
        s = s
    a = " "
    while a not in 'sn':
        a = str(input("Quer incluir mais pessoas? [N/S]: ")).strip().lower()[0]
    if a in "n":
        break
print(f"Ao total foram cadastradas {contp} pessoas, sendo {contmasc} homens e {contfem} mulheres.")
print(f"Foram cadastradas {contfem20} mulheres com menos de 20 anos.")