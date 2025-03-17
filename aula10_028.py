from random import randint
from time import sleep
computador=randint(0,5) 
print(f'Pensei em un número , tente advinhar!')
print('processando')
sleep(2)
jogador=int(input('Em que número eu pensei?'))
if jogador ==computador:
    print('Parabéns! Você conseguiu me vencer..')
else:
    print(f'Ganhei! Eu pensei no número {computador} !')
