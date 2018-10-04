# coding: utf-8
# Perimetro de um triângulo
# Eduardo Pereira / Programação 1
# sendo um triangulo ABC
import math
# Coordenadas 
coordenada_A_ponto_x = int(raw_input())
coordenada_A_ponto_y = int(raw_input())
coordenada_B_ponto_x = int(raw_input())
coordenada_B_ponto_y = int(raw_input())
coordenada_C_ponto_x = int(raw_input())
coordenada_C_ponto_y = int(raw_input())
# Cálculo das distâncis
distancia_A_B = math.sqrt((coordenada_B_ponto_x - coordenada_A_ponto_x) ** 2 + (coordenada_B_ponto_y - coordenada_A_ponto_y) ** 2)
distancia_B_C = math.sqrt((coordenada_C_ponto_x - coordenada_B_ponto_x) ** 2 + (coordenada_C_ponto_y - coordenada_B_ponto_y) ** 2)
distancia_C_A = math.sqrt((coordenada_A_ponto_x - coordenada_C_ponto_x) ** 2 + (coordenada_A_ponto_y - coordenada_C_ponto_y) ** 2)
# Cálculo do perímetro
perimetro = distancia_A_B + distancia_B_C + distancia_C_A
print'O perímetro é de %.2f' % perimetro
