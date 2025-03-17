prim=int(input('Digite o primeiro termo: '))
razao=int(input('Digite a razão: '))
termo=prim
cont=1
while cont <=10:
    print(f'{termo} _',end='')
    cont+=1
    termo+=razao
print('Fim!')