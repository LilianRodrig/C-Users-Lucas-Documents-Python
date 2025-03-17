num1=int(input('digite um valor:'))
num2=int(input('digite outro valor: '))
num3=int(input('digite outro valor: '))
if num1<num2 and num1<num3:
    menor=num1
if num2<num1 and num2<num3:
    menor=num2
if num3<num1 and num3<num2:
    menor=num3
      
if num1>num2 and num1>num3:
    maior=num1
if num2>num1 and num2>num3:
    maior=num2
if num3>num1 and num3>num2:
    maior=num3
print(f'O valor menor digitado é {menor}.')
print(f'O valor maior digitado é {maior}.')
