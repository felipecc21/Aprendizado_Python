print('Pintando Parede \n')
alt = float(input('Digite a altura da parede em metros: '))
lar = float(input('Digite a largura da parede em metros: '))
area = alt * lar
tinta = area/2
print(f'Sua parede possui {alt}m de altura e {lar}m de largura, a área total dela é de {area}m²')
print(f'Para pintar essa parede será nescessario {tinta}L de tinta. ')
