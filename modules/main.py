from WordEmbedding import *
from Course import *
from Core import *
from Discipline import *
import time

if __name__ == '__main__':

	course1 = Course("BCC", "USP")
	course2 = Course("BCC 2", "USP")

	arq1 = open("../gradeBCC.txt")
	arq1 = arq1.readlines()
	len1 = len(arq1)

	arq2 = open("../gradeBCC.txt")
	arq2 = arq2.readlines()
	len2 = len(arq2)

	i = 0
	while i < max(len1, len2):

		begin = time.time()

		if (i < len1):
			name = arq1[i]
			description = arq1[i+1]

			course1.addDiscipline(name, description)			# inserting a new discipline in your respective core of the course 1

		
		if (i < len2):
			name = arq2[i]										# returning to the original value of i for the iteration in second loop
			description = arq2[i+1]

			course2.addDiscipline(name, description)
		
		end = time.time()

		print("[{0}] {1:.2f}".format(i, end - begin) + 's')
		#print('{0:.2f}'.format(end - begin) + 's')
		i += 3		

		if (i>3):
			break

	print('/////Course 1/////')
	for k in course1.cores:
		print('\n\n***{0}***'.format(k))
		for discipline in course1.cores[k].disciplines:
			#print('- {0}\n- {1}'.format(discipline.name, discipline.description))
			print(discipline)



	print('{0}%'.format(100*course1.compare(course2)))


		
''' TESTE DO SORTCORE
from gradeComparisson import *

teste = gradesComparator();

file = open('../wordcloud_BCC.txt');

for line in file:
	print(line)
	line = file.readline()
	#print("Ementa = " + line)	
	print(teste.getDisciplineCore(line))
	line = file.readline()
	#print(" ")
'''