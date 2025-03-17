dia=int(input('Digite a quantidade de dias que está com o carro:'))
km=float(input('digite a quantidade de km que rodou com o carro :'))
vldia=dia*60
vlkm=km*0.15
print(f'Você terá que pagar R${vldia+vlkm:.2f} sendo R${vldia:.2f} pela quantidade de dias e R${vlkm:.2f} pela quantidade de km rodado.')