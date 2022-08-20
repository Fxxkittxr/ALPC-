'''
Faça um algoritmo que calcule o valor de reembolso de despesas de combustível 
de um funcionário. Considere que o carro tem o consumo de 1 litro de gasolina 
a cada 13km rodado. E o preço do litro de gasolina é de R$ 2,20.
'''

print ("Insira o valor de km rodados: ")
km = int(input())
total = int()
total = (2.20 / 13) * km
print ("O valor a ser reembolsado é de: R$",total)