from random import randint
computador=randint(1,10) 
print(f'Pensei em un número de 1 à 10 , tente advinhar!')
acertou=False
palpites=0
while not acertou:
    jogador=int(input('Qual seu palpite? '))
    palpites+=1
    if jogador ==computador:
        acertou=True
    else:
        if jogador<computador:
            print('Mais..tente mais uma vez.')
        elif jogador>computador:
            print('Menos..tente novamente')
            
print(f'Parabéns! Você conseguiu me vencer na {palpites}º tentativa .')
