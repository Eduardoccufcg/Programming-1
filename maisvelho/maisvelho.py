# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Mais Velhos Primeiro


def idosos_inicio(fila):
	j = 0
	for i in range(len(fila)):
         if fila[i] >= 60:
            fila[i],fila[j] = fila[j],fila[i]
            j += 1

