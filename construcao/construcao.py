# coding: utf-8
# Eduardo Pereira / Programação 1
largura_terreno = float(raw_input())
comprimento_terreno = float(raw_input())
area_1_casa = float(raw_input())
area_terreno = float((largura_terreno * comprimento_terreno) / area_1_casa)

print'%d casa(s) pode(m) ser construída(s) no terreno.' % int(area_terreno)
