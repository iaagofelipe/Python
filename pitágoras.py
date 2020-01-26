catOp = float(input('Digite o cateto oposto: '))
catAdj = float(input('Digite o cateto adjacente: '))
hipotenusa = (catAdj ** 2 + catOp ** 2) ** (1/2)
print('O valor da hipotenusa é {:.2f}'.format(hipotenusa))
