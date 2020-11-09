vendedor = str(input())
salario = float(input())
total_vendas_mes = float(input())

total = (total_vendas_mes * 0.15) + salario

print('TOTAL = R$ %.2f' % total)