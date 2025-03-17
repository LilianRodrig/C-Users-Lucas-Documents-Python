nota1=float(input('Digite aprimeira nota do aluno: '))
nota2=float(input('Digite a segunda nota do aluno: '))
media=(nota1+nota2)/2
print(f'A media de nota do aluno é {media} .')
if media >=5 and media < 7:
    print('O aluno está em recuperação.')
elif media <5:
    print('O aluno está reporvado')
else:
    print('O aluno está aprovado')
    