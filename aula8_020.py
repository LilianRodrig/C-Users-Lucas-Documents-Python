from random import shuffle
aluno1=str(input('digite o nome do primeiro aluno: '))
aluno2=str(input('digite o nome do segundo aluno: '))
aluno3=str(input('digite o nome do terceiro alno: '))
aluno4=str(input('digite o nome do quarto aluno: '))
lista=[aluno1,aluno2,aluno3,aluno4]
shuffle(lista)
print(f' A ordem de apresentação será:  ')
print(lista)
