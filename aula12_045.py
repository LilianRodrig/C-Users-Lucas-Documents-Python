from random import randint
itens=('Pedra', 'Papel','Tesoura')
computador=randint(0,2)
print('{:=^40}'.format('Vamos Jogar!'))
print('''
    JO
    KEN
    PÔ!''')
jogador=int(input('Qual a opção? 0-Pedra 1-Papel 2-Tesoura: '))
print(f'Computador jogou {itens[computador]}')
print(f'Você jogo {itens[jogador]}')
if computador==0:
    if jogador==0:
        print('Empate.')
    elif jogador==1:
        print('Você ganhou!')
    elif jogador==2:
        print('Computador ganhou!')
if computador==1:
    if jogador==0:
        print('Computador ganhou!')
    elif jogador==1:
        print('Empate')
    elif jogador==2:
        print('Você ganhou!')
if computador==2:
    if jogador==0:
        print('Você ganhou!')
    elif jogador==1:
        print('Computador ganhou!')
    elif jogador==2:
        print('Empate.')

