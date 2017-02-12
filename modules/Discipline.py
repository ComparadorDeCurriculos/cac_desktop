from WordEmbedding import *
import math

class Discipline:
	
	# static dictionary of sbc where the key is the name of the core and the value is the embedding
	sbcCores = dict({'Fundamentos de Computação'		: wordEmbedding(open('nucleos/fundamentos.txt').read()),
					 'Tecnologias de Computação'		: wordEmbedding(open('nucleos/tecnologias.txt').read()),
					 'Matemática'						: wordEmbedding(open('nucleos/matematica.txt').read()),
					 'Ciências Básicas'					: wordEmbedding(open('nucleos/ciencias.txt').read()),
					 'Eletrônica'						: wordEmbedding(open('nucleos/eletronica.txt').read()),
					 'Contexto Social e Profissional'	: wordEmbedding(open('nucleos/profissional.txt').read())})

	def __init__(self, name, description, credtis):
		self.name = name
		self.description = description
		self.embedding = wordEmbedding(self.name + ' ' + self.description)
		self.credtis = credtis
		self.setDisciplineCore()

		### teste para a disciplina Laboratório de Física Geral I ###
		'''
		if (name == 'Laboratório de Física Geral I'):
			print(name)
			print(self.embedding.words)
			print('\n\nCiências Básicas')
			print(Discipline.sbcCores['Ciências Básicas'].words)
			print('\n\n' + self.coreName)
			print(Discipline.sbcCores[self.coreName].words)

			disc = self.embedding.words
			comp = Discipline.sbcCores['Ciências Básicas'].words
			#comp = Discipline.sbcCores[self.coreName].words

			# comparando dsiciplina 

			vetDisc = []
			vetComp = []
			# preenchendo bag of words
			bow = list(disc)
			for w in comp:
				try:
					bow.index(w)
				except:
					bow.append(w)

			for w in bow:
				try:
					disc.index(w)
						
					vetDisc.append(1)
				except:
					vetDisc.append(0)

				try:
					comp.index(w)
					vetComp.append(1)
				except:
					vetComp.append(0)

			print('\nbow\n{0}\n\nvetDisc\n{1}\n\nvetComp\n{2}'.format(bow, vetDisc, vetComp))

			prod = 0
			nDisc = 0
			nComp = 0
			for i in range(len(bow)):
				prod += vetDisc[i] * vetComp[i]
				nDisc += math.pow(vetDisc[i], 2)
				nComp += math.pow(vetComp[i], 2)

			nDisc = math.sqrt(nDisc)
			nComp = math.sqrt(nComp)
			print('COS = {0:.2f}%'.format(prod / (nDisc * nComp) * 100))'''
			
	def setDisciplineCore(self):

		biggestScore = -1

		for coreTemp in Discipline.sbcCores:
			score = self.embedding.compare(Discipline.sbcCores[coreTemp])
			if (score > biggestScore):
				biggestScore = score
				self.coreName = coreTemp