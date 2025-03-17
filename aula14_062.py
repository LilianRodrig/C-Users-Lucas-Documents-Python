prim=int(input('Digite o primeiro termo: '))
razao=int(input('Digite a razão: '))
termo=prim
cont=1
total=0
mais=10
while mais!=0:
    total+=mais
    while cont <=total:
        print(f'{termo} _',end='')
        cont+=1
        termo+=razao
    print('Puasa')
    mais=int(input('Quantos termos você deseja vê a mais? '))
print(f'Progressão foi finalizada com {total} de termos mostrados.')

