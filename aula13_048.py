soma=0
for m in range (1,501,2):
    if m %3==0:
        soma=soma+m
print(f'A soma dos numeros multiplos de 3 de 1 até 500 é igual a {soma}')