# coding: utf-8
# Concurso
# Eduardo Pereira / Programação 1

nota_1_candidato_1 = float(raw_input())
nota_2_candidato_1 = float(raw_input())
nota_3_candidato_1 = float(raw_input())
idade_candidato_1 = int(raw_input())

nota_1_candidato_2 = float(raw_input())
nota_2_candidato_2 = float(raw_input())
nota_3_candidato_2 = float(raw_input())
idade_candidato_2 = int(raw_input())

media_candidato_1 = (nota_1_candidato_1 * 0.3) + (nota_2_candidato_1 * 0.4) + (nota_3_candidato_1 * 0.3)
media_candidato_2 = (nota_1_candidato_2 * 0.3) + (nota_2_candidato_2 * 0.4) + (nota_3_candidato_2 * 0.3)

if media_candidato_1 > media_candidato_2 or media_candidato_1 == media_candidato_2 and idade_candidato_1 > idade_candidato_2:
	print'O primeiro candidato foi aprovado com média %.1f.' % media_candidato_1
elif media_candidato_1 < media_candidato_2 or media_candidato_1 == media_candidato_2 and idade_candidato_1 < idade_candidato_2:
	print'O segundo candidato foi aprovado com média %.1f.' % media_candidato_2
else: 
	print'Empate.'
		
