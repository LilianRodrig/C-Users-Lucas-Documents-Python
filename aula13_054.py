from datetime import date
atual=date.today().year
totmaior=0
totmenor=0
for pess in range (1,8):
    ano=float(input(f'Em que ano a {pess}º pessoa nasceu? '))
    idade=atual-ano
    if idade >=18:
         totmaior+=1
    else:
        totmenor+=1
print(f'Ao todos temos {totmaior} pessoas maior de idade e {totmenor} menor de idade.')