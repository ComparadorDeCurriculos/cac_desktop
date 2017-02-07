from WordEmbedding import *
from Core import *
from Discipline import *

class Course:

	def __init__(self, name, university, path):
		self.name = name
		self.university = university
		#each core contains a list of disciplines that belong to that core and a number respective to the credits of the disciplines
		self.cores = {'Fundamentos de Computação'	 : {'credits': 0, 'disciplines':[]}, 
			  		'Tecnologias de Computação'		 : {'credits': 0, 'disciplines':[]}, 
			  		'Matemática' 					 : {'credits': 0, 'disciplines':[]}, 
			  		'Ciências Básicas'				 : {'credits': 0, 'disciplines':[]}, 
			  		'Eletrônica'					 : {'credits': 0, 'disciplines':[]}, 
			  		'Contexto Social e Profissional' : {'credits': 0, 'disciplines':[]}}
		self.path = path
		self.fillCourse();

	#adds a discipline 
	def addDiscipline(self, name, description, credits):
		discipline = Discipline(name, description)
		#inserting the discipline in the core 'disciplines' list
		self.cores[discipline.coreName]['disciplines'].append(discipline);
		#increasing the number of credits of each core 'credits' field
		self.cores[discipline.coreName]['credits'] += credits;
	
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

	def createEmbedding(self):
		self.fillCourse()

		text = ''
		for k in self.cores:
			for discipline in self.cores[k].disciplines:
				text = text + ' ' + discipline.name + ' ' + discipline.description

		self.embedding = wordEmbedding(text) 

	def compare(self, course):
		result = self.embedding.compare(course.embedding)
		return result

	# returns a list of disciplines
	def getCoreDisciplines(self, core):
		return self.cores[core]['disciplines'];

	#returns a dictionary of {core_name: n_of_credits}
	def getCoresCreditsDict(self):
		return {'Fundamentos de Computação'	 : self.cores['Fundamentos de Computação']['credits'], 
			  		'Tecnologias de Computação'		 : self.cores['Tecnologias de Computação']['credits'], 
			  		'Matemática' 					 : self.cores['Matemática']['credits'], 
			  		'Ciências Básicas'				 : self.cores['Ciências Básicas']['credits'], 
			  		'Eletrônica'					 : self.cores['Eletrônica']['credits'], 
			  		'Contexto Social e Profissional' : self.cores['Contexto Social e Profissional']['credits']}

	#returns a list of (n_of_credits)
	def getCoresCreditsList(self):
		return (self.cores['Fundamentos de Computação']['credits'], 
			  		self.cores['Tecnologias de Computação']['credits'], 
			  		self.cores['Matemática']['credits'], 
			  		self.cores['Ciências Básicas']['credits'], 
			  		self.cores['Eletrônica']['credits'], 
			  		self.cores['Contexto Social e Profissional']['credits'])
