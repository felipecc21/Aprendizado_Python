frase = str(input('Digite uma frase: ')).strip().upper()
print(f'A letra "A" aparece {frase.count("A")} vezes na frase.')
print(f'A primeira letra "A" apareceu a primeira vez na posição {frase.find("A")+1}')
print(f'A ultima letra "A" aparece na posição {frase.rfind("A")+1}')
