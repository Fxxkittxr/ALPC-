'''
Faça um programa que receba o peso de uma pessoa, calcule e mostre:
a.	O novo peso da pessoa se engordar 15% sobre o peso digitado
b.	O novo peso da pessoa se emagrecer 20% sobre o peso digitado
'''
p = int(input("Insira o seu peso atual em Kg: "))
en = p + ((p * 15 )/100)
em = p - ((p * 20 )/100)
input(f"Caso engorde 15% do peso terá {en}Kg, caso emagreça 20% terá {em}Kg")