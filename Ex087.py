matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
spar = scol = mail = 0
for l in range (0,4):
    for c in range (0,4):
        matriz[l][c] = int(input(f"Digite um valor para [{l},{c}]: "))
print("*="*30)
for l in range (0,4):
    for c in range (0,4):
        print(f"[{matriz[l][c]:^5}]",end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
for l in range (0,4):
    scol += matriz[l][2]

print("*="*30)
print(f"A soma dos números pares é {spar}")
print(f"A soma da 3ª coluna é {scol}")
for c in range(0,4):
    if c == 0:
        mail = matriz[1][c]
    elif matriz[1][c] > mail:
        mail > matriz[1][c]
print(f"O maior valor da segunda linha é o {mail}")
