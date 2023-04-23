def idade (f):
    from datetime import date
    data = date.today()
    idd = int(data.year) - f
    return idd

def voto (v):
    global i
    if i < 16:
        print('Você ainda não pode votar!')
    elif 18 > i >= 16:
        print('O seu voto é opcional!')
    else:
        print('O seu voto é obrigatório!')


#
a = int(input("Em que ano você nasceu? "))
i = (idade(a))
voto(i)