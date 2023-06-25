print('Reajuste Salarial \n')
salario = float(input('Digite o valor do seu salário atualmente: R$ '))
aumento = float(input('Digite a porcetagem de aumento: '))
calcAumento = salario + (salario*aumento/100)
diferença = calcAumento-salario
print(f'Seu salário sairá de {salario:.2f} R$ para {calcAumento:.2f} R$. Aumentando {diferença:.2f} R$.')