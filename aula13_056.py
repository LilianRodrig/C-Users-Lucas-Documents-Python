soma=0
media=0
maioridade=0
totmulher20=0
nomemaisvelho=0
for d in range (1,5):
    print(f'------- {d}º Pessoa ------- ')
    pessoa=str(input('Nome da pessoa: '))
    idade=int(input('Idade: '))
    sexo=str(input('Sexo M/F: '))
    soma+=idade
    if d==1 and sexo in 'Mm':
        maioridade=idade
        nomemaisvelho=pessoa
    if sexo in 'Mm' and idade >maioridade:
        maioridade=idade
        nomevelho=pessoa
    if sexo in 'Ff' and idade <20:
        totmulher20+=1
media=soma/4
print(f'A média da idade é {media}. ')
print(f'O homem mais velho tem {maioridade} anos e se chama {nomevelho}.')
print(f'Temos {totmulher20} mulheres com menos de 20 anos. ')
