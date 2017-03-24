from WordEmbedding import *
import math
import re

#reads file in path and builds a SBCCores dictionary from it.
#the file format should be:
# 		{Core Name}
#		Discipline Name
#		Discipline description
#		Discipline credits count
#the {Core Name} should be used only when starting a new disciplines core list.
#the discipline credits count is currently not being used 
def buildSBCCoresDict(path):
		disciplines = {}
		currentCore = None;
		with open(path) as f:
			for lines in f:
				try:
					#checks if line contains something
					lines = lines.rstrip();

					#checks for the core delimiter ("{ }")

					result = re.match('{(.*?)}',lines)
					if(result):
						#if found text between '{}', creates a new core
						currentCore = result.group(1);
						disciplines[currentCore] = [];
						lines = next(f).rstrip();

					#gets discipline name
					name = lines;

					#gets discipline description
					desc = next(f).rstrip();

					#gets next line; However, we do not need it.
					next(f);

					disciplines[currentCore].append((name,wordEmbedding(name + " " + desc)))
				except:
					pass

		return disciplines

class Discipline:

	# static dictionary of sbc where the key is the name of the core and the value is the embedding

	sbcCores = buildSBCCoresDict('nucleos/computacao_ref.txt');

	def __init__(self, name, description, credits):
		self.name = name
		self.description = description
		self.embedding = wordEmbedding(self.name + ' ' + self.description)
		self.credits = credits
		self.setDisciplineCore()
			
	def setDisciplineCore(self):

		winnerCore = ''
		winnerEmbedding = None
		biggestScore = -1

		#for every SBC core:
		for cores in Discipline.sbcCores:
			#for every discipline in each core:
			for coreDisciplines in Discipline.sbcCores[cores]:
				#unzips the 'coreDiscipline' structure into a name and an embedding
				name, emb = coreDisciplines

				#calculate score and checks if it is the highest
				score = self.embedding.compare(emb)
				if(score > biggestScore):
					biggestScore = score;
					winnerCore = cores;
					self.coreName = cores;
