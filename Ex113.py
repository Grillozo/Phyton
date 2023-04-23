def leiaint(n):
    while True:
        try:
            n = int(input("Digite um número: "))

        except KeyboardInterrupt:
            print("Usuário não digitou valor nenhum.")
            break
        except:
            print("Valor inválido")
            continue
        else:
            print(f'você digitou o valor {n}')
            return n

def leiafloat(num):
    while True:
        try:
            num = float(input("Digite um número decimal: "))
        except KeyboardInterrupt:
            print("O usuário não digitou valor nenhum.")
            return 0
        except:
            print('Valor inválido!')
            continue
        else:
            print(f'Você digitou o valor {num}')
            return n
# Programa Principal
n = ''
num = ''
leiaint(n)
leiafloat(num)
