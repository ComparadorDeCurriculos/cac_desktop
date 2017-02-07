from WordEmbedding import *
from Core import *
from Discipline import *
import time

class Course:

	def __init__(self, name, university, path):
		self.name = name
		self.university = university
		#each core contains a list of disciplines that belong to that core
		self.cores = {'Fundamentos de Computação'	 : {'credits': 0, 'disciplines':[]}, 
			  		'Tecnologias de Computação'		 : {'credits': 0, 'disciplines':[]}, 
			  		'Matemática' 					 : {'credits': 0, 'disciplines':[]}, 
			  		'Ciências Básicas'				 : {'credits': 0, 'disciplines':[]}, 
			  		'Eletrônica'					 : {'credits': 0, 'disciplines':[]}, 
			  		'Contexto Social e Profissional' : {'credits': 0, 'disciplines':[]}}
		self.path = path
		self.fillCourse();

	def addDiscipline(self, name, description,credits):
		discipline = Discipline(name, description)						# creating discipline
		self.cores[discipline.coreName]['disciplines'].append(discipline);
		self.cores[discipline.coreName]['credits'] += credits;				# adding in your respective core
				
	def fillCourse(self):
		with open(self.path) as f:
			for lines in f:
				try:
					#checks if line contains something
					lines = lines.rstrip();

					#gets discipline name
					name = lines;

					#gets discipline description
					desc = next(f).rstrip();

					#gets discipline credits no.
					cred = int(next(f).rstrip());
				except StopIteration:
					pass
				self.addDiscipline(name,desc,cred); 

	def createEmbedding(self):
		self.fillCourse()

		text = ''
		for k in self.cores:
			for discipline in self.cores[k].disciplines:
				text = text + ' ' + discipline.name + ' ' + discipline.description

		self.embedding = wordEmbedding(text) 


	def compare(self, course):
		
		result = self.embedding.compare(course.embedding)
		
		# print("Time to compare {0:.2f}s".format(end - begin))
		
		return result

	def getCoreDisciplines(self,core):
		return self.cores[core]['disciplines'];

	def getCoresCredits(self):
		return {'Fundamentos de Computação'	 : self.cores['Fundamentos de Computação']['credits'], 
			  		'Tecnologias de Computação'		 : self.cores['Tecnologias de Computação']['credits'], 
			  		'Matemática' 					 : self.cores['Matemática']['credits'], 
			  		'Ciências Básicas'				 : self.cores['Ciências Básicas']['credits'], 
			  		'Eletrônica'					 : self.cores['Eletrônica']['credits'], 
			  		'Contexto Social e Profissional' : self.cores['Contexto Social e Profissional']['credits']}
