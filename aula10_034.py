salario=float(input('Digite o salario do funcionario: R$ '))
if salario <2000:
    print(f'O funcionario irá receber R$ {(salario*15/100)+salario:.2f}')
else:
    print(f'O funcionario irá receber R$ {(salario*10/100)+salario:.2f}')