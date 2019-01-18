import sys

def main():
	expr = input("Escreva a expressão a calcular: ")
	print('\nResultado da expressão: ')
	print(evaluate(parse(tokenize(expr))))
	print('\nExpressão escrita de forma regular: ')
	print(converter(parse(tokenize(expr))))
	print('\nRetorno do tokenize(): ')
	print(tokenize(expr))
	print('\nRetorno do parse(): ')
	print(parse(tokenize(expr)))
	print('\nValores das variáveis no dicionário: ')
	testHashtable()

def tokenize(stri):
	l = []
	#Adicionou-se casos de 3,4,5 espaços para permitir erros de escrita no nº de espaços ao inserir a expressão
	stri = stri.replace("     "," ")
	stri = stri.replace("    "," ")
	stri = stri.replace("   "," ")
	stri = stri.replace("(","( ")
	stri = stri.replace(")"," )")
	stri = stri.replace("  "," ")
	l = stri.split(" ")
	return l

def parse(token):
	l = []
	iterat = iter(token)
	next(iterat) #ignora o primeiro '('
	while True:
		l += (parseREC(iterat),)
		if (next(iterat, None) == None):
			break
	if (l == [] or None in l):
		print("A expressão inserida não está correta. Verifique a sintaxe!")
		sys.exit(1)
	return l

def parseREC(iterat):
	tup = ()
	for i in iterat:
		if (i == '('):
			tup += ( parseREC(iterat), )
		elif (i.isdigit()): 
			tup += (int(i),)
		elif ( i == ')'): 
			return tup
		else:
			tup += (i,)

def evaluate(parsedList):
	for i in parsedList:
		res = evaluateREC(i)
	return res

def evaluateREC(i):
	if (i[0] == 'define'):
			hashtableVars[i[1]] = i[2]
			return
	else:
		try:
			if (i[0] == '+'):
				if (isinstance(i[1],tuple) and isinstance(i[2],tuple)):
					return evaluateREC(i[1]) + evaluateREC(i[2])
				elif (isinstance(i[1],tuple)):
					if (isinstance(i[2],str)):
						return evaluateREC(i[1]) + hashtableVars[i[2]]	
					else:
						return evaluateREC(i[1]) + i[2]	
				elif (isinstance(i[2],tuple)):
					if (isinstance(i[1],str)):
						return hashtableVars[i[1]] + evaluateREC(i[2])
					else:
						return i[1] + evaluateREC(i[2])
				else:
					if (isinstance(i[1],str) and isinstance(i[2],str)):
						return hashtableVars[i[1]] + hashtableVars[i[2]]
					elif (isinstance(i[1],str)):
						return hashtableVars[i[1]] + i[2]
					elif (isinstance(i[2],str)):
						return i[1] + hashtableVars[i[2]]
					else: 
						return i[1] + i[2]
			elif (i[0] == '-'):
				if (isinstance(i[1],tuple) and isinstance(i[2],tuple)):
						return evaluateREC(i[1]) - evaluateREC(i[2])
				elif (isinstance(i[1],tuple)):
					if (isinstance(i[2],str)):
						return evaluateREC(i[1]) - hashtableVars[i[2]]	
					else:
						return evaluateREC(i[1]) - i[2]	
				elif (isinstance(i[2],tuple)):
					if (isinstance(i[1],str)):
						return hashtableVars[i[1]] - evaluateREC(i[2])
					else:
						return i[1] - evaluateREC(i[2])
				else:
					if (isinstance(i[1],str) and isinstance(i[2],str)):
						return hashtableVars[i[1]] - hashtableVars[i[2]]
					elif (isinstance(i[1],str)):
						return hashtableVars[i[1]] - i[2]
					elif (isinstance(i[2],str)):
						return i[1] - hashtableVars[i[2]]
					else: 
						return i[1] - i[2]
			elif (i[0] == '*'):
				if (isinstance(i[1],tuple) and isinstance(i[2],tuple)):
					return evaluateREC(i[1]) * evaluateREC(i[2])
				elif (isinstance(i[1],tuple)):
					if (isinstance(i[2],str)):
						return evaluateREC(i[1]) * hashtableVars[i[2]]	
					else:
						return evaluateREC(i[1]) * i[2]	
				elif (isinstance(i[2],tuple)):
					if (isinstance(i[1],str)):
						return hashtableVars[i[1]] * evaluateREC(i[2])
					else:
						return i[1] * evaluateREC(i[2])
				else:
					if (isinstance(i[1],str) and isinstance(i[2],str)):
						return hashtableVars[i[1]] * hashtableVars[i[2]]
					elif (isinstance(i[1],str)):
						return hashtableVars[i[1]] * i[2]
					elif (isinstance(i[2],str)):
						return i[1] * hashtableVars[i[2]]
					else: 
						return i[1] * i[2]
			elif (i[0] == '/'):
				if (isinstance(i[1],tuple) and isinstance(i[2],tuple)):
					return evaluateREC(i[1]) / evaluateREC(i[2])
				elif (isinstance(i[1],tuple)):
					if (isinstance(i[2],str)):
						return evaluateREC(i[1]) / hashtableVars[i[2]]	
					else:
						return evaluateREC(i[1]) / i[2]	
				elif (isinstance(i[2],tuple)):
					if (isinstance(i[1],str)):
						return hashtableVars[i[1]] / evaluateREC(i[2])
					else:
						return i[1] / evaluateREC(i[2])
				else:
					if (isinstance(i[1],str) and isinstance(i[2],str)):
						return hashtableVars[i[1]] / hashtableVars[i[2]]
					elif (isinstance(i[1],str)):
						return hashtableVars[i[1]] / i[2]
					elif (isinstance(i[2],str)):
						return i[1] / hashtableVars[i[2]]
					else: 
						return i[1] / i[2]
			elif (i[0] == 'mod'):
				if (isinstance(i[1],tuple) and isinstance(i[2],tuple)):
					return evaluateREC(i[1]) % evaluateREC(i[2])
				elif (isinstance(i[1],tuple)):
					if (isinstance(i[2],str)):
						return evaluateREC(i[1]) % hashtableVars[i[2]]	
					else:
						return evaluateREC(i[1]) % i[2]	
				elif (isinstance(i[2],tuple)):
					if (isinstance(i[1],str)):
						return hashtableVars[i[1]] % evaluateREC(i[2])
					else:
						return i[1] % evaluateREC(i[2])
				else:
					if (isinstance(i[1],str) and isinstance(i[2],str)):
						return hashtableVars[i[1]] % hashtableVars[i[2]]
					elif (isinstance(i[1],str)):
						return hashtableVars[i[1]] % i[2]
					elif (isinstance(i[2],str)):
						return i[1] % hashtableVars[i[2]]
					else: 
						return i[1] % i[2]
			else:
				print("O programa encontrou um operador inesperado! Os operados disponíveis são: + , - , * , / , mod ")
				sys.exit(1)
		except KeyError:
			print('A expressão contém uma ou mais variáveis não definidas! Verifique a expressão inserida')
			sys.exit(1)

#FUNÇÕES EXTRA
#converter() e converterREC() - Convertem a expressão para o modo tradicional de leitura

def converter(parsed):
	l = []
	iterat = iter(parsed)
	for i in iterat:
		if (i[0] != 'define'):
			expr = converterREC(i)
	expr = expr.replace('  ',' ')
	return expr

def converterREC(i):
	final = ""
	if (isinstance(i[1],tuple) and isinstance(i[2],tuple)):
		final = final + ' ( ' + converterREC(i[1]) + ' ) ' + str(i[0]) + ' ( ' + converterREC(i[2]) + ' ) '	
	elif (isinstance(i[1],tuple)):
		final = final + ' ( ' + converterREC(i[1]) + ' ) ' + str(i[0]) + ' ' + str(i[2])
	elif (isinstance(i[2],tuple)):
		final = final + ' ' + str(i[1]) + ' ' + str(i[0]) + ' ( ' + converterREC(i[2]) + ' ) '
	else:
		final = final + ' ' + str(i[1]) + ' ' + str(i[0]) + ' ' + str(i[2])
	return final

#Imprime a hashtable/dicionário de variáveis

def testHashtable():
		print(hashtableVars)

hashtableVars = {}
main()