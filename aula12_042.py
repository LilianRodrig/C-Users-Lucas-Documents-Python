num1=float(input('Primeiro segmento:'))
num2=float(input('Segundo seguimento: '))
num3=float(input('Terceiro segmento: '))
if num1<num2 +num3 and num2<num1+num3 and num3<num1+num2:
    print('Os segmentos podem formar um triangulo.')
    if num1==num2==num3:
        print('Equilatero. ')
    elif num1!=num2!=num3!=num1:
        print('Escaleno.')
    else:
        print('Isósceles.')