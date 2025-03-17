vlr=float(input('Digite o valor da casa: '))
gnh=float(input('Qual o valor do seu salario? '))
anos=int(input('Quantos anos você pretende pagar? '))
prestação= vlr/(anos*12)
print(f'para pagar o valor de uma casa no valor de R${vlr:.2f} em {anos} , a prestação será de R${prestação:.2f}.')

if prestação<=gnh*30/100:
    print(f' O banco libera o emprestimo para você.')
else:
    print(f'O banco não libera o emprestimo para você.')