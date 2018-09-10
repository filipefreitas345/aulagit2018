"""
Autor: Filipe Medrado Freitas
Data: 22/08/2018

Questão 03
"""
lista = list()

for x in range(5):
    numero = int(input('Digite um numero:'))
    
    if len(lista) == 0 or lista[-1] < numero:
        lista.append(numero)
        continue
    
    pos = 0
    while numero > lista[pos]:
        pos = pos + 1
        
    # .insert = inserir
    lista.insert(pos, numero)

print(lista)
