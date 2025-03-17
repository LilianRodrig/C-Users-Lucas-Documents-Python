print('{:=^40}'.format('Lojas Pepetins'))
vlr=float(input('Valor da compra: '))
print('''Formas de pagamento
    [1] à vista
    [2]À vista no cartão
    [3]2x no cartão
    [4]3x ou mais no cartão''')
opção=int(input('Qual a opção?'))
if opção==1:
    print(f'Total será R$ {vlr-(vlr*10/100)}.')
elif opção==2:
    print(f'Total será R$ {vlr-(vlr*5/100)}.')
elif opção==3:
    print(f'Total será R$ {vlr}.')
elif opção==4:
    prcl=int(input('Quantas parcelas? '))
    print(f'Total será R$ {vlr+(vlr*20/100)} sendo {prcl} parcelas de R$ {(vlr+(vlr*20/100))/7:.2f}.')
    