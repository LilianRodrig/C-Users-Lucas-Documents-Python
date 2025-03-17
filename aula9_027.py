nome=str(input('Digite seu nome completo: ')).strip()
n=nome.split()
print(f'Prazer em te conhecer {nome} , seu primeiro nome é {n[0]} , e seu ultimo nome é {n[len(n)-1]}.')