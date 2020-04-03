"""
Aula (esta entre aula 007 e 008)
Desafio 14
Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF
"""
c = float(input('Informe a temperatura em ºC: '))
f = ((9*c) / 5) +32 # neste caso não precisa de parenteses, pois segue a ordem de presedência
print("A temperatura de {}ºC correspode a {:.2f}ºF".format(c, f))
