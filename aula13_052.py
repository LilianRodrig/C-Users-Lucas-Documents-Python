total=0
num=int(input('Digite um número:'))
for p in range(1,num+1):
    if num%p==0:
        print('\033[34m ',end=' ')
        total=total+1
    else:
        print('\033[m',end=' ')
    print(f'{p}',end=' ')
print()
print(f'O número {num} foi divisível {total} vezes.')
