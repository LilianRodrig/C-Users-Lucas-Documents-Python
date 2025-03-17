print('='*30)
print('{:^30}'.format('Banco PPTIN'))
print('='*30)
valor=int(input('Qual valor deseja sacar? R$'))
total=valor
ced=50
totcedu=0
while True:
    if total>=ced:
        total-=ced
        totcedu+=1
    else:
        if totcedu>0:
            print(f'Total de {totcedu} cédulas de R${ced}')
        if ced==50:
            ced=20
        elif ced==20:
            ced=10
        elif ced==10:
            ced=1
        totcedu=0
        if total==0:
            break
         
print('='*30)
print('Volte sempre ao banco PPTIN!')