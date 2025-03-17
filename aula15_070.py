total=0
valor=0
barato=0
cont=0
while True:
    produto=str(input('Nome do produto: '))
    preço=float(input('Preço: R$ '))
    cont+=1
    total+=preço
    if preço>1000:
        valor+=1
    if cont==1:
        barato=preço
    else:
        if preço<barato:
            barato=preço
    resp=' '
    while resp not in 'SN':
        resp=str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp=='N':
            break
print(f'**** FIM DO PROGRAMA! ****')
print(f'O valor total das compras foi de {total:.2f}')
print(f'Temos {valor} produtos custando mais de R$1000')
print(f'O produto mais barato custou {barato:.2f}')
