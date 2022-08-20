'''
Faça um algoritmo que calcule o percentual de espaço livre de um HD, sabendo 
que o HD tem o tamanho máximo de 40.000 megabytes. Solicite a quantidade livre 
em megabytes.
'''
print ("Infome a quantidade livre em megabytes:")
ml = int(input())
l = (ml * 100)/40000
print("A porcentagem de megabyte livre é:", l,"%")