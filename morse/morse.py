# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Tradutor Morse
lista = []
def tradutor_morse(lista):
	traducao = ''
	for d in range(len(lista)):
		if lista[d] == '.-':
			traducao += 'a'
		elif lista[d] == '-...':
			traducao += 'b'	
		elif lista[d] == '-.-.':
			traducao += 'c'	
		elif lista[d] == '-..':
			traducao += 'd'	
		elif lista[d] == '.':
			traducao += 'e'	
		elif lista[d] == '..-.':
			traducao += 'f'	
		elif lista[d] == '--.':
			traducao += 'g'
		elif lista[d] == '....':
			traducao += 'h'	
		elif lista[d] == '..':
			traducao += 'i'	
		elif lista[d] == '.---':
			traducao += 'j'
		elif lista[d] == '-.-':
			traducao += 'k'
		elif lista[d] == '.-..':
			traducao += 'l'
		elif lista[d] == '--':
			traducao += 'm'	
		elif lista[d] == '-.':
			traducao += 'n'	
		elif lista[d] == '---':
			traducao += 'o'	
		elif lista[d] == '.--.':
			traducao += 'p'	
		elif lista[d] == '--.-':
			traducao += 'q'	
		elif lista[d] == '.-.':
			traducao += 'r'
		elif lista[d] == '...':
			traducao += 's'	
		elif lista[d] == '-':
			traducao += 't'	
		elif lista[d] == '..-':
			traducao += 'u'
		elif lista[d] == '...-':
			traducao += 'v'		
		elif lista[d] == '.--':
			traducao += 'w'		
		elif lista[d] == '-..-':
			traducao += 'x'		
		elif lista[d] == '-.--':
			traducao += 'y'		
		elif lista[d] == '--..':
			traducao += 'z'		
	return traducao

			
