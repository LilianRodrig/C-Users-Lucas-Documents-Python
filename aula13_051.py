prim=int(input('Digite o primeiro termo: '))
razao=int(input('Digite a razão: '))
decimo=prim+(10-1)*razao
for p in range(prim,decimo,razao):
    print(f'{p}', end='_')
print('Fim!')