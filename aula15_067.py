while True:
    num=int(input('Quer ver a tabuada de qual número ? '))
    if num <0:
        break
    for m in range(1,11):
        print(f'{num} x {m} ={num*m}')
print('Programa encerrado, volte sempre!')