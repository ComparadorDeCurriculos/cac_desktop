from WordEmbedding import *

class Core:
	name = ""
	disciplines = []	# list of disciplines
	credtis = 0
	embedding = None

	def __init__(self, name):
		self.name = name
		self.disciplines = []
		self.credtis = 0
		self.embedding = wordEmbedding('')

	def addDiscipline(self, discipline):
		# addding disciplines to the core
		self.disciplines.append(discipline)
		# adding credtis to the core
		self.credtis += discipline.credtis
		# appending embedding of the core
		self.embedding.appendBoW(discipline.name + ' ' + discipline.description)

	def compare(self, core):
		return self.embedding.compare(core.embedding)