from WordEmbedding import *

class Core:

	def __init__(self, name):
		self.name = name
		self.disciplines = []
		self.credits = 0

	def addDiscipline(self, discipline):
		# addding disciplines to the core
		self.disciplines.append(discipline)
		# adding credits to the core
		self.credits += discipline.credits

class Discipline:

	# static dictionary of SBC Cores:
	# the key is the name of the core and the value is a list of disciplines
	sbcCores = None

	def __init__(self, name, description, credits, core = None):
		self.name = name
		self.description = description
		self.embedding = wordEmbedding(self.name + ' ' + self.description)
		self.credits = credits
		self.core = core

	def classifyCore(self,reference):

		winnerCore = ''
		winnerEmbedding = None
		biggestScore = -1


		# for every core in reference cores:
		for core in reference.cores:
			#for every discipline in reference core:
			for refDiscipline in reference.cores[core].disciplines:

				#calculate score
				score = self.embedding.compare(refDiscipline.embedding)
				#checks if it is the highest yet
				if(score > biggestScore):
					biggestScore = score;
					winnerCore = core;
					self.core = core;

class Course:

	def __init__(self, name, university, path, reference = None):
		self.name = name
		self.university = university
		self.cores = {}
		self.path = path
		self.fillCourse(reference);

	#gets all disciplines from the course file, classificates it in the cores dictionary and counts the number of credits in each core			
	def fillCourse(self, reference):
		#when using a reference, this variable will remain as None
		#when not using a reference, this variable will hold the current core being read in the reference file
		currentCore = None

		if reference is None:
			#regular expression is needed for reference course construction
			import re
		else:
			for core in reference.cores:
				self.cores[core] = Core(core);

		#the "with open(file) as f" statement handles file opening and closing
		with open(self.path) as f:
			#iterates through each line in the file
			for lines in f:
				try:
					#checks if line contains something
					lines = lines.rstrip();

					#If there is no reference course, then this is a reference course
					if(reference is None):

						#checks for the core delimiter ("{ }")
						result = re.match('{(.*?)}',lines)
						if(result):
							#creates a new core with the name found between "{}"
							currentCore = result.group(1);
							self.cores[currentCore] = Core(currentCore);

							#fetching next line for disciplines
							lines = next(f).rstrip();

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
				discipline = Discipline(name, desc, cred, currentCore)

				#If there is a reference, then uses it to classify the discipline
				if reference is not None:
					discipline.classifyCore(reference);

				#inserts discipline in core
				self.cores[discipline.core].addDiscipline(discipline)

	# returns a list of disciplines
	def getCoreDisciplines(self, coreName):
		return self.cores[coreName].disciplines

	#returns a dictionary of {core_name: n_of_credits}
	def getCoresCreditsDict(self):
		return {name : self.cores[name].credits for name in self.cores}

	#returns a list of [n_of_credits]
	def getCoresCreditsList(self):
		return [self.cores[name].credits for name in self.cores]