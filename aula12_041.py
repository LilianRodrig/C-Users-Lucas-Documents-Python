from datetime import date
ano=int(input('Qual seu ano de nascimento? '))
idade=date.today().year - ano
print(f'O atleta tem {idade} anos.')
if idade<=9:
    print('A classificação é Mirin.')
elif idade >9 and idade<=14:
    print('A classificação é Infantil.')
elif idade>14 and idade <=19:
    print('A classificação é Jr.')
elif idade >19 and idade <=25:
    print('A classificação é Sênior')
elif idade>25:
    print('A classificação é Master.')