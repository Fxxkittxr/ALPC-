'''
Construa um algoritmo que calcule a quantidade total de ração
consumida por um cachorro por mês. Solicite a quantidade consumida
por refeição e o numero de refeições por dia.
'''
print ("Insira a quantidade consumida em uma refeição em g: ")
qnt = int(input())
print ("Insira o número de refeições que é feita por dia: ")
rd = int(input())
qt = (qnt * rd) * 30
qtkg = qt /100
print ("A quantidade total de ração consumida é de:", qt, "g ou", qtkg, "kg")