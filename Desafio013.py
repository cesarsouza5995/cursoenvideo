"""
Aula 7
Desafio 13
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.
"""
sal = float(input('Digite o valor do Salário R$ '))
sala = sal + (sal * 15/100)
print('Salário atual R${:.2f}, Com aumento R${:.2f}'.format(sal, sala))