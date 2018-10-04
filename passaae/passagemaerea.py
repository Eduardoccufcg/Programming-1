# coding: utf-8
# Eduardo Pereira / Programação 1
distancia_milhas = float(raw_input())
aliquota = float(raw_input())
valor_passagem = float((distancia_milhas * aliquota) + 51.00)
opcao1 = float(valor_passagem * 0.75)
opcao2 = float(valor_passagem * 0.95)
opcao2_parce = float(opcao2 / 6)
print'Valor da passagem: R$ %.2f' % valor_passagem
print'\nPagamento:'
print'1. À vista. R$ %.2f' % opcao1
print'2. Em 6 parcelas. Total: R$ %.2f' % opcao2
print'   6 x R$ %.2f' % opcao2_parce
print'3. Em 10 parcelas. Total: R$ %.2f' % valor_passagem
print'   10 x R$ %.2f' % (valor_passagem / 10 )

