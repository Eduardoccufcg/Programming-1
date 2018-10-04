# coding: utf-8
# MRU
# Eduardo Pereira / Programação 1
s_inicial = float(raw_input())
velocidade = float(raw_input())
tempo = float(raw_input())
s_final = s_inicial + (velocidade * tempo)
print'Posição final do móvel'
print'S(%.1f) = %.1f m' % (tempo , s_final)
