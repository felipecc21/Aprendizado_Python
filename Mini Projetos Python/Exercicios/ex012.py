print('Calculando Descontos')
item = float(input('Digite o valor total dos itens: R$'))
desconto = float(input('Digite o valor do desconto em porcentagem: '))
valorFinal = item-(item*desconto/100)
print(f'O valor tota de seus itens é de: {item} R$, foi aplicado o desconto de {desconto}'
      f' %, logo o valor final dos seus itens é de: {valorFinal:.2f} R$')
