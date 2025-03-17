import random
aluno1=str(input('digite o nome do primeiro aluno: '))
aluno2=str(input('digite o nome do segundo aluno: '))
aluno3=str(input('digite o nome do terceiro alno: '))
aluno4=str(input('digite o nome do quarto aluno: '))
lista=(aluno1,aluno2,aluno3,aluno4)
escolhido=random.choice(lista)
print(f'O aluno escolhido foi: {escolhido}')

