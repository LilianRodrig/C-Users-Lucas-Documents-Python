print('/'*20)
print('Analisador de triangulos')
print('/'*20)
num1=float(input('digite uma reta:'))
num2=float(input('digite outra reta: '))
num3=float(input('digite outra reta: '))

if num1<num2 +num3 and num2<num1+num3 and num3<num1+num2:
    print('Os segmentos acima podem formar o triangulo.')
else:
    print('Os segmentos acima não podem formar um triangulo.')