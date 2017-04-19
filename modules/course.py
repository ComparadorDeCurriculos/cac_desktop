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
			#regular expression is needed for building a reference course
			import re
		else:
			#if a reference exists, creates cores with the same structure as the 
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


	def compare(self, course, threshold):

		a = []	# unique disciplines of self
		b = []	# unique disciplines of course
		ab = []	# equivalent disciplines between self and course
		eqs = []


		# iterating on course 1 disciplines
		for core in self.cores:
			for disc in self.cores[core].disciplines:
				score = 0
				maxscore = 0
				# iterating on course 2 disciplines
				#a += 1 # counting number of disciplines in course 1
				for core2 in course.cores:
					for disc2 in course.cores[core2].disciplines:
						# b += 1 # counting number of disciplines in course 2
						score = disc.embedding.compare(disc2.embedding)
						if score > maxscore:
							maxscore = score
							discEq = (score, disc, disc2)

				if maxscore >= threshold:
					#filling ab
					ab.append(discEq)
					eqs.append(discEq[2])
				else:
					#filling a
					a.append(disc)

		#filling b			
		for core in course.cores:
			for disc in course.cores[core].disciplines:
				if disc not in eqs:
					b.append(disc);

		return (a, b, ab)


	def printComparisson(self, result):

		equivalents = result[2]
		# ordenando
		i = 0
		while i < len(equivalents) :
			k = i
			maior = 0
			while k < len(equivalents) :
				if (equivalents[k][0] > maior) :
					maior = equivalents[k][0]
					temp = equivalents.pop(k)
					equivalents.insert(i, temp)
				k += 1
			i += 1

		#printando 
		for eq in equivalents:
			print('{0:.2f} => {1} <-> {2}'.format(eq[0], eq[1].name, eq[2].name))


		print("========a========")

		for disc in result[0]:
			print(disc.name);

		print("========b========")

		for disc in result[1]:
			print(disc.name);


	# returns a list of disciplines
	def getCoreDisciplines(self, coreName):
		return self.cores[coreName].disciplines

	#returns a dictionary of {core_name: n_of_credits}
	def getCoresCreditsDict(self):
		return {name : self.cores[name].credits for name in self.cores}

	#returns a list of [n_of_credits]
	def getCoresCreditsList(self):
		return [self.cores[name].credits for name in self.cores]