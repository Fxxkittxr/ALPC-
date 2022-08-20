'''
Escreva um algoritmo que calcule o valor de uma chamada de telefone. Deverá ser informado a quantidade de minutos falados durante a ligação além de sua origem. Considere que uma ligação “local” custa R$0.020, ligação “intermunicipal” R$0,08 e “interestadual” R$0,1.
'''
ql = int(input("Informe a quantidade de minutos usados na ligação:"))
lgc = str(input("Informe se a ligação foi Local(L), Intermunicipal(M) ou Interestadual(E):"))
if lgc == "L":
    L = 0.02 * ql
    print(f"A ligação custou R${L} ")
else:
  if lgc == "E":
      E = 0.1 * ql
      print(f"A ligação custou R${E} ")
      
  else:
      if lgc == "M":
          M = 0.08 * ql
          print(f"A ligação custou R${M} ")
      else:
            print("Opção Inexistente.")