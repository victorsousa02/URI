peca1, quant_peca1, val_peca1 = input().split()
peca2, quant_peca2, val_peca2 = input().split()

peca1 = int(peca1)
quant_peca1 = int(quant_peca1)
val_peca1 = float(val_peca1)
peca2 = int(peca2)
quant_peca2 = int(quant_peca2)
val_peca2 = float(val_peca2)

total = (quant_peca1 * val_peca1) + (quant_peca2 * val_peca2)

print('VALOR A PAGAR: R$ %.2f' % total)
