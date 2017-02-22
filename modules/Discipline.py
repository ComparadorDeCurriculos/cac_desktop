from WordEmbedding import *
import math

def getCoreDisciplines(path):
	disciplines = []
	with open(path) as f:
		for lines in f:
			try:
				#checks if line contains something
				lines = lines.rstrip();

				#gets discipline name
				name = lines;

				#gets discipline description
				desc = next(f).rstrip();

				disciplines.append((name,wordEmbedding(name + " " + desc)))
			except:
				pass

	return disciplines

class Discipline:

	# static dictionary of sbc where the key is the name of the core and the value is the embedding
	sbcCores = dict({'Fundamentos de Computação'		: getCoreDisciplines('nucleos/fundamentos.txt'),
					 'Tecnologias de Computação'		: getCoreDisciplines('nucleos/tecnologias.txt'),
					 'Matemática'						: getCoreDisciplines('nucleos/matematica.txt'),
					 'Ciências Básicas'					: getCoreDisciplines('nucleos/ciencias.txt'),
					 'Eletrônica'						: getCoreDisciplines('nucleos/eletronica.txt'),
					 'Contexto Social e Profissional'	: getCoreDisciplines('nucleos/profissional.txt')})



	def __init__(self, name, description, credits):
		self.name = name
		self.description = description
		self.embedding = wordEmbedding(self.name + ' ' + self.description)
		self.credits = credits
		self.setDisciplineCore()
			
	def setDisciplineCore(self):

		winnerCore = ''
		winnerEmbedding = None
		biggestScore = -1

		if(self.name == 'Eletrônica para Computação'):
			for cores in Discipline.sbcCores:
				for coreDisciplines in Discipline.sbcCores[cores]:
					name, emb = coreDisciplines
					score = self.embedding.compare(emb)
					# print (name,' ',score);
					if(score > biggestScore):
						winnerName = name;
						biggestScore = score;
						winnerCore = cores;
						self.coreName = cores;
						winnerEmbedding = emb;
			# print("{0}: {1}({2})".format(self.name,winnerCore,score));
			# print("doc1 = {0}, doc2 = {1}".format(self.name,winnerName));
			# self.embedding.compare2(winnerEmbedding);
		else:
			for cores in Discipline.sbcCores:
				for coreDisciplines in Discipline.sbcCores[cores]:
					name, emb = coreDisciplines
					score = self.embedding.compare(emb)
					if(score > biggestScore):
						biggestScore = score;
						winnerCore = cores;
						self.coreName = cores;
