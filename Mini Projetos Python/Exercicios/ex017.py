'''print('Catetos e Hipotenusa \n')
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(f'A hipotenusa vai medir {hi:.2f}')'''

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimentop do cateto adjacente: '))
hi = hypot(co, ca)
print(f'O valor da hipotenusa é de {hi:.2f}')
