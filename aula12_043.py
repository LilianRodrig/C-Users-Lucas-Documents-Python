kg=float(input('Qual o seu peso? KG: '))
alt=float(input('Qual sua altura? M: '))
imc=kg/(alt**2)
print(f'O seu IMC é de {imc:.2f}')
if imc<18.5:
    print('Você está abaixo do peso!')
elif imc>=18.5 and imc<=25:
    print('Seu peso está ideal!')
elif imc>25 and imc<=30:
    print('Você está com sobrepeso, cuidado!')
elif imc>30 and imc<=40:
    print('Obesidade , se cuide!')
else:
    print('Obesidade móirbida! Mastigar não conta como atividade física!')