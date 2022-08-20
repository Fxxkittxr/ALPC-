print ("Insira o valor do primeiro número:")
pn = int(input())
print ("Insira o valor do segundo número:")
sn = int(input())
if pn > sn:
    print (pn,"é maior do que", sn)
else:
    if pn < sn:
        print (pn,"é menor do que", sn)
    else:
        print (pn,"é igual à", sn)