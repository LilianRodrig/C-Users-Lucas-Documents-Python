from random import randint
v=0
print('{:=^40}'.format('Vamos Jogar!'))
while True:
    jogador=int(input('Digite um valor: '))
    computador=randint(0,10)
    total=jogador + computador
    tipo=' '
    while tipo not in 'PI':
        tipo=str(input('Par ou Impar [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}, o total de {total}.')
    if tipo=='P':
        
        if total%2==0:
            print('Você venceu!')
            v+=1
        else:
            print('Você perdeu.')
            break
    elif tipo=='I':
        if total%2==1:
            print('Você venceu!')
            v+=1
        else:
            print('Você perdeu..')
            break
    print('Vamos jogar novamente?')
print(f'Você teve {v} vitórias!')