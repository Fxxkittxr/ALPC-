'''
Construa um algoritmo que mostre o percentual que uma despesa mensal 
representa do seu salário total.
'''
print ("Insira o valor do seu salário: ")
slr = int(input())
print ("Insira o valor da despesa mensal: ")
dm = int(input())
prct = (100 * dm) / slr
print ("O percentual do seu salário que é gasto com a despesa mensal é  igual à: ", prct)