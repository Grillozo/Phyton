n = 0
while True:
    n = int(input("Quer ver a tabuada de qual valor? \n"))
    if n < 0:
        break
    for c in range (1,11,1):
        print(f"{n} X {c} = {n*c}")
print("Programa encerrado, Obrigado!")