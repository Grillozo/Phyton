# Alistamento no Exército

from datetime import date
ano = int(input("Digite o ano de nascimento: "))
data = date.today()
idade = int(data.year) - ano
if idade == 18:
    print('Está na hora de se alistar!')
elif idade > 18:
    print('Já passou do tempo de alistamento!')
else:
    print('Ainda não é hora de se alistar!')
