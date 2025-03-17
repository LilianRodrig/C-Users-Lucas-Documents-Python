#nome=str(input('qual seu nome :'))
#if nome=="Lilian":
#   print('Que nome lindo você tem!')
#else:
#   print('Seu nome é tão normal!')   
#print(f'Bom dia {nome}!')

n1=float(input('Digite sua primeira nota: '))
n2=float(input('Digite sua segunda nota: '))
m=(n1 + n2)/2
print(f'A sua média de nota é {m:.1f}')
if m >=6.0:
    print(f'Sua média foi boa, parabéns!')
else:
    print(f'Sua média está baixa, estude mais !')
    