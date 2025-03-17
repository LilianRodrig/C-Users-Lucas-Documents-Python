velocidade = float(input('Qual a velocidade do carro ?'))
if velocidade > 80:
    print(f'Multado! Você excedeu o limite maximo permitido!')
    multa=(velocidade-80)*7
    print(f'Você receberá uma multa de R${multa:.2f}')
else:
    print('Tenha uma boa viagem! Dirija com segurança!')