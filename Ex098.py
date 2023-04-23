from time import sleep
def cont (i, f, p):
    if 0 > p == 0:
        p = 1
    print(i, end="-")
    if i < f:
        while i < (f-p):
            print(i+p, end="-")
            sleep(0.5)
            i += p
    if i > f:
        while i > (f+p):
            print(i-p, end="-")
            sleep(0.5)
            i -= p


#Programa
print("="*22)
print("BEM VINDO AO CONTADOR")
print("="*22)

ini = int(input("Digite o número inicial: "))
fim = int(input("Digite o número final:   "))
pas = int(input("Digite o passo:          "))


cont (ini, fim, pas)






