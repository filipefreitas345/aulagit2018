"""
Autor: Filipe Medrado Freitas
Data: 22/08/2018

Questão 05
"""
todos_numeros = list()

while True:
     numero = int(input('Digite um numero: '))
     todos_numeros.append(numero)
     resp = input('Deseja sair? n/s')

     if resp == 's':
         break

numeros_pares = list()
numeros_impares = list()

for x in todos_numeros:
    if x % 2 == 0:
        numeros_pares.append(x)
    else:
        numeros_impares.append(x)

print(todos_numeros)
print(numeros_pares)
print(numeros_impares)
