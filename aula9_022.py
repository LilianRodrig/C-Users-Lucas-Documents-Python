
frase=str(input('Digite seu nome completo: '))
print(f'Seu nome em maiúsculo é: {frase.upper()}')
print(f'Seu nome minúsculo é: {frase.lower()}')
print(f'Seu nome todo tem {len(frase)-frase.count(" ")}')
print(f'Seu primero nome tem {frase.find(" ")}')
separa=frase.split()
print(f'Seu primeiro nome é {separa[0]}, e ele tem {len(separa[0])}')

#dividido=frase.count()
#print(dividido[0])