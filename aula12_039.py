from datetime import date
ano=int(input('Digite seu ano de nascimento:'))
#atual=date.today().year
idade=date.today().year -ano
if idade<18:
    print(f'Faltam {idade-18} para você se alistar')
elif idade>18:
    print(f'Você já tinha que ter se alistado a {idade-18} anos atras')
elif idade==18:
    print(f'Você precisa se alistar o mais breve possível!')
