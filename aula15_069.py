maio=0
masc=0
fem=0
while True:
    idade=int(input('Idade: '))
    sexo=' '
    while sexo not in 'FM':
        sexo=(str(input(' Digite o seu sexo [F/M]: '))).strip().upper()[0]
    if idade>=18:
        maio+=1
    if sexo=='M':
        masc+=1
    if idade>=20 and sexo=='F':
        fem+=1
    resp=' '
    while resp not in 'S/N':
        resp=str(input('Que continuar ? [S/N]: ')).strip().upper()[0]
    if resp=='N':
        break
print(f'No total temos {maio} pessoas maior de idade , {masc} homens cadastrados e {fem} mulheres maior de 20 anos.')
        