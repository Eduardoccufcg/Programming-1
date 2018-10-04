# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Resolve Vizinhos


def resolve_vizinhos(seq):
	for i in range(len(seq)-1,-1,-1):
		if seq[i-1] == seq[i] and seq[i] == seq[i-2]:
			seq[i-2] += 2
			seq[i-1] += 1
		elif seq[i-1] == seq[i]:
			if seq[i-1] + 1 == seq[i-2]:
				seq[i-1] += 2
			else:
				seq[i-1] += 1
