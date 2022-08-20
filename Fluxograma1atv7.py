'''
Faça um algoritmo que calcule o valor da multa por atraso de pagamento 
de um boleto bancário. Solicite o valor do boleto e o percentual de multa.
'''
print("insira o valor do boleto bancário(R$):")
bb = int(input())
print("insira o percentual da multa (%):")
pm = int(input())
print("insira o numero de dias de atraso:")
da = int(input())
tt = bb + (bb * (pm / 100) * da)
print ("Total a ser pago:", tt)