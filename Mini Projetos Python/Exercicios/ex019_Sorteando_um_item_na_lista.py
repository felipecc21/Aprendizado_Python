import random
print(f'Sorteando um item na lista \n')
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n4, n2, n3, n1]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi: {escolhido}')

