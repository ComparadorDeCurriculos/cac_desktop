from WordEmbedding import *

class Discipline:
	
	name = ""
	description = ""
	embedding = None
	coreName = ""		# core of discipline
	equivalent = [] 	# list of disicplines

	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.embedding = wordEmbedding(self.name + ' ' + self.description)
		self.setDisciplineCore()


	def setDisciplineCore(self):

		biggestScore = -1
		result = None
		cores = {}

		cores = dict({'Fundamentos de Computação'		: wordEmbedding(open('../nucleos/fundamentos.txt').read()),
					  'Tecnologias de Computação'		: wordEmbedding(open('../nucleos/tecnologias.txt').read()),
					  'Matemática'						: wordEmbedding(open('../nucleos/matematica.txt').read()),
					  'Ciências Básicas'				: wordEmbedding(open('../nucleos/ciencias.txt').read()),
					  'Eletrônica'						: wordEmbedding(open('../nucleos/eletronica.txt').read()),
					  'Contexto Social e Profissional'	: wordEmbedding(open('../nucleos/profissional.txt').read())})

		for coreTemp in cores:
			score = self.embedding.compare(cores[coreTemp])
			if (score > biggestScore):
				biggestScore = score
				self.coreName = coreTemp
			#print("parsing {0:s} done".format(core));
			# print(core,':{1:.0f}%'.format(core,score*100));