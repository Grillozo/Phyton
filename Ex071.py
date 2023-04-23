#bank ATM
'''v = int(input("Input the ammount you want to withdraw: "))
u = v // 1 % 10
d = v // 10 % 10
c = v // 100 % 10
m = v // 1000 % 10

print(f"Você irá receber: \n{u} notas de Rdolar1.")
print(f"{d} notas de Rdolar10.")
print(f"{c*2} notas de Rdolar50.")
print(f"{m*10} notas de Rdolar100.")'''

v = int(input("Input the ammount you want to withdraw: "))
total = v
bill50 = bill20 = bill10 = bill1 = 0

while True:
    if total > 50:
        total -= 50
        bill50 += 1
    elif total > 20:
        total -= 20
        bill20 += 1
    elif total > 10:
        total -= 10
        bill10 += 1
    elif total >= 1:
        total -= 1
        bill1 += 1
    else:
        break
print (f"You will get:\n "
       f"{bill50} fifty dolar bills.\n "
       f"{bill20} twenty dolar bills.\n "
       f"{bill10} ten dolar bills.\n "
       f"{bill1} one dolar bills. ")