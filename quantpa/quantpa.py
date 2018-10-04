# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Quantas PAs
quantas_pa = 0
n = 0
razao = int(raw_input())

while True:
	seq = raw_input()
	seqs = seq.split()
	if seq == 'fim':
		break
	for d in range(len(seqs) -1):
		if int(seqs[d +1]) - int(seqs[d]) == razao:
			n += 1
	if n == len(seqs) -1:
		quantas_pa += 1
	n = 0
		
print quantas_pa
