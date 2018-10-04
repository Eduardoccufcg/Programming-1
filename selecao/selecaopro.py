# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Seleção Projeto

CRE_candidato = float(raw_input())
experiencia_em_meses = float(raw_input())
nota_entrevista = float(raw_input())

if CRE_candidato < 7 and experiencia_em_meses < 6:
	print'Candidato eliminado. CRE e experiência abaixo do limite.'
elif CRE_candidato < 7:
	print'Candidato eliminado. CRE abaixo do limite.'
elif experiencia_em_meses < 6:
	print'Candidato eliminado. Experiência abaixo do limite.'
if CRE_candidato >= 7 and experiencia_em_meses >= 6:
	if nota_entrevista <= 3:
		print'Candidato classificado.'
	elif nota_entrevista > 3:
		print'Candidato aprovado.'
