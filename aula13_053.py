frase=str(input('Digite uma frase: ')).strip().upper()
palavras=frase.split() 
junto=''.join(palavras) 
print(f'Você digitou a frase {palavras}')
print(f'Você digitou a frase{junto}.')
inverso=''
for l in range(len(junto)-1,-1,-1):
    inverso+=junto[l]
print(f'A frase ao inverso fica {inverso}.')
if  inverso==junto:
    print('Temos um palíndromo.')
else:
    print(' A frase não é um palíndromo.')