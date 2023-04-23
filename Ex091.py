#Jogo de dados (usando dicionário)
from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
jogadores ['jogador1'] = randint(1,6)
jogadores ['jogador2'] = randint(1,6)
jogadores ['jogador3'] = randint(1,6)
jogadores ['jogador4'] = randint(1,6)
ranking = {}
print(jogadores)
print("=-"*30)
ranking = sorted(jogadores.items(),key=itemgetter(1), reverse=True)
for k,v in enumerate(ranking):
    print (f"{k+1}º lugar: {v[0]} com {v[1]}")
    sleep(1)
