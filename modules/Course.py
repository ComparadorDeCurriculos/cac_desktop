from WordEmbedding import *
from Core import *
from Discipline import *

class Course:

	def __init__(self, name, university, path):
		self.name = name
		self.university = university
		self.cores = {'Fundamentos de Computação' 	   : Core('Fundamentos de Computação'),
					  'Tecnologias de Computação' 	   : Core('Tecnologias de Computação'),
					  'Matemática'				  	   : Core('Matemática'),
					  'Ciências Básicas'		  	   : Core('Ciências Básicas'),
					  'Eletrônica'				  	   : Core('Eletrônica'),
					  'Contexto Social e Profissional' : Core('Contexto Social e Profissional')}
		self.path = path
		self.fillCourse();

	#adds a discipline 
	def addDiscipline(self, name, description, credits):
		discipline = Discipline(name, description, credits)
		#inserting the discipline in the core 
		self.cores[discipline.coreName].addDiscipline(discipline)

	#gets all disciplines from the course file, classificates it in the cores dictionary and counts the number of credits in each core			
	def fillCourse(self):
		#the "with open(file) as f" statement handles file opening and closing
		with open(self.path) as f:
			#iterates through each line in the file
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
					#this exception happens when I try to iterate through the end of the file
					pass

				#adds the new discipline
				self.addDiscipline(name,desc,cred); 

	# returns a list of disciplines
	def getCoreDisciplines(self, coreName):
		return self.cores[coreName].disciplines

	#returns a dictionary of {core_name: n_of_credits}
	def getCoresCreditsDict(self):
		return {name : self.cores[name].credits for name in self.cores}

	#returns a list of [n_of_credits]
	def getCoresCreditsList(self):
		return [self.cores[name].credits for name in self.cores]
