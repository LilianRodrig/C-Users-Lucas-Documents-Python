soma=0
cont=0
for n in range(1,7):
    n1=int(input(f'Digite o {n} valor: '))
    if n1%2==0:
        soma+=n1
        cont+=1
print(f'Você informou {cont} números pares e a soma entre eles é {soma}')
