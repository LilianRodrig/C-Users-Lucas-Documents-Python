resp='s'
soma=0
quant=0
media=0
maior=0
menor=0
while resp in 'Ss':
    num=int(input('Digite um número: '))
    soma+=num
    quant+=1
    if quant==1:
        maior=menor=num
    else:
        if num>maior:
            maior=num
        if num<menor:
            menor=num
    resp=str(input('Quer continuar?[s/n] ')).upper().strip()[0]
media=soma/quant   
print(f'Você digitou {quant} números e a média foi {media}.') 
print(f'O maior valor digitado foi {maior} e o menor foi {menor}.')