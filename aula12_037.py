num=int(input('Digite um número inteiro: '))
conv=int(input('DIgite uma conversão: 1-Binário 2-Octal  3-Hexadecimal: '))
binario=bin(num)[2:]
octal= oct(num)[2:]
hexadecimal= hex(num)[2:]
if conv==1:
    print(f'{conv} convertido paa binário é igual a {binario}')
elif conv==2:
    print(f'{conv} convertido para octal é igual a {octal}')
elif conv==3:
    print(f'{conv} convertido para hexadecimal é igual a {hexadecimal}')
else:
    print('Opção inválida, tente novamente.')