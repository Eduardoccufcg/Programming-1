#coding: utf -8
# (c) 2017, Eduardo Pereira, UFCG, Programação 1
import math
velocidade_de_vazao = float(raw_input())
diametro_cano = float(raw_input()) 
tempo = float(raw_input())
seccao = float((math.pi * diametro_cano**2) / 4)
vazao = velocidade_de_vazao * seccao * 1000            #convertendo para litros                                           #em segundos
quantidade_de_agua = tempo * vazao
print "Quantidade de água =", quantidade_de_agua, "litros."
