
seq = [3,1,2,3,10,5,6]
seq2 = []
i = 0
for j in range(1,len(seq)):
	if  j != len(seq): 
		if seq[i] < seq[i-1]:
			seq2.append(seq[j])
	i += 2
print seq2
