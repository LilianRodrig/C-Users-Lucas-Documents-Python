from time import sleep
num1=int(input('Digite o primeiro valor: '))
num2=int(input('Digite o segundo valor: '))
opção=0
maior=0
while opção !=5: 
    print('''Digite uma opção  :
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opção=int(input('>>>>>>Qual a sua opção?'))
    if opção==1:
        print(f'O resultado da opção desejada é {num1+num2}')
    elif opção==2:
        print(f'O resultado da opção desejada é {num1*num2}')
    elif opção==3:
        if num1>num2:
            print(f'O numero maior digitado é {num1}.')       
        else:
            print(f'O numero maior digitado é {num2}')        
    elif opção==4:
        num1=int(input('Digite o primeiro valor: '))
        num2=int(input('Digite o segundo valor: '))
    elif opção==5:
        print('Finalizando')
    else:
        print('Opção invalida!')
sleep(2)  
print('Fim do programa, volte quando quiser!')


