# coding: utf-8
# Área de uma esfera
# Eduardo Pereira / Programação 1

print'== Estágio 1 =='
peso1 = float(raw_input('Peso? '))
nota1 = float(raw_input('Nota? '))
print '== Estágio 2 =='
peso2 = float(raw_input('Peso? '))
nota2 = float(raw_input('Nota? '))
print '== Estágio 3 =='
peso3 = float(raw_input('Peso? '))
nota3 = float(raw_input('Nota? '))
# Cálculo da Media Parcial e Medias finais para passar
media_parcial = nota1 * peso1 + nota2 * peso2 + nota3 * peso3
media_para_5 = (media_parcial * 0.6 - 5.0) / 0.4 * -1
media_para_7 = (media_parcial * 0.6 - 7.0) / 0.4 * -1
print'== Resultados =='
print'Média parcial:',media_parcial
print'Nota na final, pra média 5.0 = %.1f' % media_para_5
print'Nota na final, pra média 7.0 = %.1f' % media_para_7

