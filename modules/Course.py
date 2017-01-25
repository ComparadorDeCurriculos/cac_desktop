from WordEmbedding import *
from Core import *
from Discipline import *
import time

class Course:
	
	name = ""
	university = ""
	cores = {}		
	path = ""	
	embedding = None


	def __init__(self, name, university, path):
		self.name = name
		self.university = university
		self.cores = dict({	'Fundamentos de Computação'		 : Core('Fundamentos de Computação'), 
					  		'Tecnologias de Computação'		 : Core('Tecnologias de Computação'), 
					  		'Matemática' 					 : Core('Matemática'), 
					  		'Ciências Básicas'				 : Core('Ciências Básicas'), 
					  		'Eletrônica'					 : Core('Eletrônica'), 
					  		'Contexto Social e Profissional' : Core('Contexto Social e Profissional')})
		self.path = path
		self.createEmbedding()

	def addDiscipline(self, name, description):
		discipline = Discipline(name, description)						# creating discipline
		self.cores[discipline.coreName].addDiscipline(discipline)		# adding in your respective core
			
	def fillCourse(self):
		file = open(self.path)
		file = file.readlines()
		lenFile = len(file)

		i = 0
		while i < lenFile:
			begin = time.time()

			name = file[i]									# read line i   == name of discipline
			description = file[i+1]							# read line i+1 == description of discipline 
			self.addDiscipline(name, description)			# inserting a new discipline in your respective core of the course 1

			end = time.time()

			print("{0:.2f}s - {1}".format(end - begin, name))
			i += 3											# the third line is invalid, because of this is the increase by three in three

	def createEmbedding(self):
		self.fillCourse()

		text = ''
		for k in self.cores:
			for discipline in self.cores[k].disciplines:
				text = text + ' ' + discipline.name + ' ' + discipline.description

		self.embedding = wordEmbedding(text) 


	def compare(self, course):
		begin = time.time()
		result = self.embedding.compare(course.embedding)
		end = time.time()
		
		print("Time to compare {0:.2f}s".format(end - begin))
		
		return result
