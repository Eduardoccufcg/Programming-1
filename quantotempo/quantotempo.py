# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Diferença entre Dois Horários no Dia

def quanto_tempo(horario1,horario2):

	hora1 = int(horario1[0] + horario1[1]) * 60
	minutos1 = int(horario1[3] + horario1[4])
	minutos_total1 = hora1 + minutos1

	hora2 = int(horario2[0] + horario2[1]) * 60
	minutos2 = int(horario2[3] + horario2[4])
	minutos_total2 = hora2 + minutos2

	minutos_novo = (minutos_total2 - minutos_total1) % 60
	hora_nova = (minutos_total2 - minutos_total1) / 60

	return '%d hora(s) e %d minuto(s)' % (hora_nova,minutos_novo)

