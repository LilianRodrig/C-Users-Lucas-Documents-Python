import math
angulo=float(input('Digite uma angulo que você deseja:'))
seno=math.sin(math.radians(angulo))
cosseno=math.cos(math.radians(angulo))
tangente=math.tan(math.radians(angulo))
print(f'O seno será {seno:.2f} , o valor do cosseno será {cosseno:.2f} e a tangente será {tangente:.2f}')