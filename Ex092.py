#Calculo de aposentadoria (utilizando dicionário)
from datetime import datetime
info={}
today = datetime.today()
while True:
    info["nome"] = str(input("Nome: "))
    ano = int(input("Ano de nascimento: "))
    info["idade"] = today.year - ano
    info["ctps"] = int(input("Carteira de trabalho(0 não tem): "))
    if info["ctps"] == 0:
        print("=*"*30)
        print(f'Nome: {info["nome"]}\n'
              f'Idade: {info["idade"]}')
        print("Não possui carteira de Trabalho")
        break
    else:
        info["contratacao"] = int(input("Ano de contratação: "))
        info["salario"] = float(input("Salário: "))
        info["aposentadoria"] = info["idade"] + (35 - (today.year - info["contratacao"]))
        print("=*"*30)
        for a, i in info.items():
            print(f"{a}: {i}".title())
        print("=*"*30)
        break
