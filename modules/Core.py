class Core:

	name = ""
	disciplines = []	# list of disciplines
	simSBC = 0.0		# similarity to the SBC core
	simComp = 0.0		# similarity to the comparassion core 

	def __init__(self, name):
		self.name = name

	def addDiscipline(self, discipline):
		self.disciplines.append(discipline)