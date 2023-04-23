# Lottery number generator

from time import sleep
from random import randint

print("\033[32mWelcome to the Lotto Generator!\033[m ")
n = int(input("Type in the number of sequences you want me to generate: "))
jogos = []
temp = []
print(f"\033[34mRandomizing... Please Wait!\033[m")
print("=-"*17)
for l in range (0,n):
    for j in range(0,6):
        rand = randint(1,60)
        temp.append(rand)
        if j == 5:
            jogos.append(sorted(temp)[:])
            temp.clear()
    sleep(1)
    print(f"Entry {l+1}: {jogos[l]}")
print("=-"*17)
print("\033[34mGood Luck! I hope you hit the Jackpot!")