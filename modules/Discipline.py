from WordEmbedding import *

class Discipline:
	
	name = ""
	description = ""
	embedding = None
	coreName = ""		# core of discipline
	# static dictionary of sbc where the key is the name of the core and the value is the embedding
	sbcCores = dict({'Fundamentos de Computação'		: wordEmbedding(open('../nucleos/fundamentos.txt').read()),
					 'Tecnologias de Computação'		: wordEmbedding(open('../nucleos/tecnologias.txt').read()),
					 'Matemática'						: wordEmbedding(open('../nucleos/matematica.txt').read()),
					 'Ciências Básicas'					: wordEmbedding(open('../nucleos/ciencias.txt').read()),
					 'Eletrônica'						: wordEmbedding(open('../nucleos/eletronica.txt').read()),
					 'Contexto Social e Profissional'	: wordEmbedding(open('../nucleos/profissional.txt').read())})


	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.embedding = wordEmbedding(self.name + ' ' + self.description)
		self.setDisciplineCore()

	def setDisciplineCore(self):

		biggestScore = -1

		for coreTemp in Discipline.sbcCores:
			score = self.embedding.compare(Discipline.sbcCores[coreTemp])
			if (score > biggestScore):
				biggestScore = score
				self.coreName = coreTemp
			#print("parsing {0:s} done".format(core));
			#print(core,':{1:.0f}%'.format(core,score*100));