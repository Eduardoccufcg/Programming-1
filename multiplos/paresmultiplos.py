# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Descarta facilmente



seq = raw_input().split()
n = float(raw_input())
pares = []

for i in range(1, len(seq)):
    
    if float(seq[i]) / float(seq[i - 1]) == n:
        pares.append('%s %s'%(seq[i - 1], seq[i]))
        
    if float(seq[i - 1]) / float(seq[i]) == n:
        pares.append('%s %s'%(seq[i - 1], seq[i]))
        
    else:
        pass
        
print'%d par(es)' % len(pares)

for n in pares:
    print n
