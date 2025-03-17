#from math import factorial  
num=int(input('Digite um número para calcular seu fatorial: '))
#f=factorial(num)
#print(f'O fatorial de {num} ´´e {f}')
c=num
f=1
print(f'Calculando {num}!=', end='')
while c>0:
    print(f'{c}', end='')
    print(f'x' if c>1 else'=',end='')
    f*=c
    c-=1
print(f'{f}')