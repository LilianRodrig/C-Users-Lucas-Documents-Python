maior=0
menor=0
for k in range (1,6):
    peso=float(input(f'Digite o peso a {k}º: '))
    if k==1:
        maior=peso
        menor=peso
    else:
        if peso>maior:
            maior=peso
        if peso<menor:
            menor=peso
print(f'O maior peso lido foi {maior} e o menor peso lido foi {menor}')
    