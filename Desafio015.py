"""
Aula (esta entre aula 007 e 008)
Desafio 15
Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias
 pelos quais foi alugado, Calcule o preço a pagar, sabendo que o carro custa R$60.00 por doa e R$0.15 por KM rodado.
"""
dias = int(input('Quantos dias alugado: '))
km = float(input('Quantos KM rodados: '))
pago = (dias * 60) + (0.15 * km)
print('Dias alugados {}\nKM rodados {}\n\nvalor a pagar R$ {:.2f}'.format(dias, km, pago))