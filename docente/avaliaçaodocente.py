# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Avaliação docente

semestres = int(raw_input())
pontuacao_ensino = float(raw_input())
pontuacao_prod_intectual = float(raw_input())
pontuacao_orientacao = float(raw_input())
pontuacao_administrativa = float(raw_input())
media = (pontuacao_administrativa + pontuacao_ensino + pontuacao_orientacao + pontuacao_prod_intectual) / semestres

if semestres < 4:
	print "Promoção indeferida. Número de semestres insuficiente."
if semestres >= 4:
	if pontuacao_ensino < 320.0 or pontuacao_prod_intectual < 100.0 or pontuacao_orientacao < 20.0:
		print"Promoção indeferida. Pontuação mínima não alcançada."
	else:
		if media < 140.0:
			print"Promoção indeferida. Média insuficiente."	
		else:
			print "Promoção deferida. Parabéns!"
