'''
Faça um programa que receba o salário-base de um funcionário, 
calcule e mostre o salário a receber, sabendo-se que esse
funcionário tem gratificação de 5% sobre o salário base e 
paga imposto de 7% sobre o salário-base.
'''
import math
sb = int(input("Informe o valor do seu salário-base: "))
sbt = sb - ((sb * 2)/100 )
g = (sb * 5)/100
imp =(sb * 7)/100
input(f"O sua gratificação é igual à:{g}")
input(f"O seu imposto é igual à:{imp}")
input(f"O seu salário total fica igual à:{sbt}")