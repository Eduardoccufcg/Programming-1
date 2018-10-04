# coding: utf-8
# IPTU
# Eduardo Pereira / Programação 1

area_construida = float(raw_input('Área construída? '))
aliquota = float(raw_input('Alíquota? ' ))
iptu = float((area_construida * aliquota) + 35.00)
        # Formas de pagamento
cota_unica = float(iptu * 0.75)
opcao2 = float(iptu * 0.95)
opcao2_parcelado = float(opcao2 / 6)
opcao_3_em10 = float(iptu / 10 )         
print 'IPTU: R$ %.2f' % iptu

print'\nPagamento:'
print'1. Quota única. R$ %.2f' % cota_unica
print'2. Em 6 parcelas. Total: R$ %.2f' % opcao2
print'   6 x R$ %.2f' % opcao2_parcelado
print'3. Em 10 parcelas. Total: R$ %.2f' % iptu
print'   10 x R$ %.2f' % opcao_3_em10

