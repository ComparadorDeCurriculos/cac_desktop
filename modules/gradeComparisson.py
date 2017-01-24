# -*- coding: iso-8859-15 -*-
from WordEmbedding import *

class gradesComparator:

	def __init__(self):

		self.cores = {'Fundamentos de Computação' : wordEmbedding(open('../nucleos/fundamentos.txt').read()), 'Tecnologias de Computação' : wordEmbedding(open('../nucleos/tecnologias.txt').read()), 'Matemática' : wordEmbedding(open('../nucleos/matematica.txt').read()), 'Ciências Básicas' : wordEmbedding(open('../nucleos/ciencias.txt').read()), 'Eletrônica' : wordEmbedding(open('../nucleos/eletronica.txt').read()), 'Contexto Social e Profissional' : wordEmbedding(open('../nucleos/profissional.txt').read())};
		print("Done");

	def getDisciplineCore(self, disciplineDescription):

		biggestScore = -1;
		result = None;
		discipline = wordEmbedding(disciplineDescription);

		for core in self.cores:
			score = discipline.compare(self.cores[core]);
			if (score > biggestScore):
				biggestScore = score;
				result = core;
			#print("parsing {0:s} done".format(core));
			# print(core,':{1:.0f}%'.format(core,score*100));

		return result;