'''
Escreva um algoritmo que calcule o numero de prateleiras necessárias para guardar uma quantidade informada de livros. Considerando que em média uma prateleira comporta 32 livros.
'''
import math
l = int(input("Informe a quantidade de livros:"))
p = l / 32
print(f"quantidade de estantes é {math.ceil(p)} para guardar {l}")