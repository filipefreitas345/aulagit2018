"""
Autor: Filipe Medrado Freitas
Data: 21/08/2018

Questão 01
"""
lista = list()

for n in range(5):
    numero = int(input('Digite um numero: '))
    lista.append(numero)

maior = max(lista)
menor = min(lista)
pos_max = lista.index(maior)
pos_min = lista.index(menor)


print('O maior numero digitado foi {} e está na posiçao {}.'.format(maior, pos_max))
print('O menor numero digitado foi {} e está na posição {}.'.format(menor, pos_min))


