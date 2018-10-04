#coding: utf -8
# (c) 2017, Eduardo Pereira, UFCG, Programação 1
valor_total = float(raw_input())
data = (raw_input())
quantidade_de_produtos = float(raw_input())

media = valor_total / quantidade_de_produtos
print 'Data:',data
print 'O valor total da compra foi de R$ %.2f. A média do preço dos produtos é de %.1f.' % (valor_total,media)
