'''
Peça 3 números pro usuário e verifique se os 3 números formam um triângulo equilátero, escaleno ou isosceles
'''
'''
verificar se é um triangulo
| b - c | < a < b + c
| a - c | < b < a + c
| a - b | < c < a + b
'''
'''
1 - Não é possível construir um triângulo se a soma das medidas de dois segmentos for menor que a medida de um terceiro segmento

2 - Não é possível construir um triângulo se a soma da medida de dois segmentos for igual à medida de um terceiro segmento.

3 - É possível construir um triângulo se a soma das medidas de dois segmentos for maior que a medida de um terceiro segmento

'''
x1 = float(input("Informe um número: "))
x2 = float(input("Informe outro número: "))
x3 = float(input("Informe mais um número: "))
xI = x1 + x2 
xII = x1 + x3 
xIII = x2 + x3
if xI > x3:
    if xII > x2:
        if xIII > x1:
          if x1 == x2:
            if x1 == x3:
              print ("Triângulo Equilátero")
            else:
              print ("Triângulo Isósceles")
          else:
            if x1 == x3:
              print ("Triângulo Isósceles")
            else:
              print ("Triângulo Escaleno")
        else:
            print ("Não há como formar um triângulo")
    else: 
        print  ("Não há como formar um triângulo")
else:
  print("Não há como formar um triângulo")