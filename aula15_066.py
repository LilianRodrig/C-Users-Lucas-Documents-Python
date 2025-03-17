n=0
s=0
cont=0
while True:
    n=int(input('Digite um número [999 faz parar.] '))
    if n==999:
        break
    s+=n
    cont+=1
print(f'Você digitou {cont} números e a soma deles é {s}.')