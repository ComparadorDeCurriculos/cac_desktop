class Core:

	name = ""
	disciplines = []	# list of disciplines

	def __init__(self, name):
		self.name = name
		self.disciplines = []

	def addDiscipline(self, discipline):
		self.disciplines.append(discipline)