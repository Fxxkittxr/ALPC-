'''
O custo ao consumidor de um carro novo é a soma do preço 
da fábrica com o percentual de lucro do distribuidor e dos 
impostos aplicados ao preço de fábrica. Faça um programa 
que receba o preço de fábrica de um veículo, o percentual 
de lucro do distribuidor e o percentual de impostos. 
Calcule e mostre:
a.	O valor correspondente ao lucro do distribuidor
b.	O valor correspondente aos impostos
c.	O preço final do veículo
'''

pf = int(input("Insira o valor do preço de fábrica: "))
ld = int(input("Insira o percentual do lucro do distribuidor: "))
imp = int(input("Insira o percentual do imposto: "))

tt = pf + ((pf * ld )/100) + ((pf * imp )/100)
ldn = ((pf * ld )/100)
impn = ((pf * imp )/100)

input(f"O valor do lucro do distribuidor é igual à: {ldn}")
input(f"O valor dos impostos é igual à: {impn}")
input(f"O valor total do veiculo é igual à: {tt}")