from WordEmbedding import *
from Core import *
from Discipline import *

class Course:
	
	name = ""
	university = ""
	cores = {}			
	embedding = None


	def __init__(self, name, university):
		self.name = name
		self.university = university
		self.cores = dict({	'Fundamentos de Computação'		 : Core('Fundamentos de Computação'), 
					  		'Tecnologias de Computação'		 : Core('Tecnologias de Computação'), 
					  		'Matemática' 					 : Core('Matemática'), 
					  		'Ciências Básicas'				 : Core('Ciências Básicas'), 
					  		'Eletrônica'					 : Core('Eletrônica'), 
					  		'Contexto Social e Profissional' : Core('Contexto Social e Profissional')})


	def addDiscipline(self, name, description):
		discipline = Discipline(name, description)
		self.cores[discipline.coreName].addDiscipline(discipline)

	
	def createEmbedding(self):
		if (self.embedding != None):
			return

		text = ''
		for k in self.cores:
			for discipline in self.cores[k].disciplines:
				text = text + ' ' + discipline.name + ' ' + discipline.description

		self.embedding = wordEmbedding(text) 


	def compare(self, course):
		
		self.createEmbedding()
		course.createEmbedding()

		return self.embedding.compare(course.embedding)


	'''
	def getIndexOfCore(self, coreName):
		i = 0
		for core in self.cores:
			if (core.name == coreName):
				break
			i += 1
		
		if (i == len(self.cores))
			return -1
		else
			return i'''