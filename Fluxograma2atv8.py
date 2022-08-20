'''
Escreva um algoritmo que calcule o valor de desconto que será oferecido ao comprador de uma loja de acordo com o valor da compra: compras até R$100 desconto de 5%, compras maiores que R$ 100 e ate R$400 desconto de 10%, e acima de R$ 400 desconto de 13%. Após o calculo do valor com desconto, acrescente o valor da taxa de entrega que é de R$ 1,5 por item comprado.
'''
c = float(input("Informe o valor total da compra em reais: "))
# passar a input para a função float, para virar um número decimal

if c >= 100:
    d = c * 0.95
    print (f"Valor da compra com desconto é de R$ {d}")
else:
    if c >= 400:
        d = c * 0.9
        print (f"Valor da compra com desconto é de R$ {d}")
    else:
        d = c * 0.87
        print (f"Valor da compra com desconto é de R$ {d}")
e = int(input("Deseja solicitar a entrega da compra? Sim (1), Não (0) :"))
if e == 1:
    it = float(input("Informe a quantidade de itens comprados: "))
    tt = d + (it * 1.5)
    print(f"O total do pedido com a taxa é igual à R${tt}")
else:
        if e == 0:
            print("Agradecemos a sua compra :)")
        else:
                print ("Opção Inválida.")