class Core:

	name = ""
	disciplines = []	# list of disciplines
	simSBC = 0.0		# similarity to the SBC core

	def __init__(self, name):
		self.name = name
		self.disciplines = []
		self.simSBC = 0.0

	def addDiscipline(self, discipline):
		self.disciplines.append(discipline)