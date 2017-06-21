from course import Course
from os import listdir
import os.path
import plotting as plt
import csv
import sys

if __name__ == '__main__':

	folderIn = 'cursos/'
	folderOut = 'comparison/'
	filesList = listdir(path='cursos')
	instList = []
	courseList = ['BCC', 'BSI', 'Eng. Comp.']
	instProc = []

	# removendo arquivos antigos
	for arq in listdir(path=folderOut):
		os.remove(folderOut+arq)

	# gera lista de todas as instituições
	for f in filesList:
		inst = f.split('_')[0]
		if (instList.count(inst) == 0):
			instList.append(inst) 

	sbc = Course("Referência", "SBC", "nucleos/computacao_ref.txt")

	for i1 in instList:
		for c1 in courseList:
			# check if file not exists 
			path = folderIn+i1+'_'+c1+'.txt'
			if (not os.path.isfile(path)):
				continue

			for i2 in instList:
				# testa se já foram geradas as comprações com essa instituição 
				if (instProc.count(i2) > 0):
					continue
				
				# não precisa de percorrer novamente os cursos
				c2 = courseList[0]

				# não compara o mesmo curso
				if ((i1 == i2) and (c1 == c2)):
					continue

				# check if file not exists 
				path = folderIn+i2+'_'+c2+'.txt'
				if (not os.path.isfile(path)):
					continue

				course1 = Course(c1, i1, folderIn+i1+'_'+c1+'.txt', sbc)
				course2 = Course(c2, i2, folderIn+i2+'_'+c2+'.txt', sbc)

				# Gerando csv para gráfico Créditos Aula por Núcleo
				with open(folderOut+'credAulaNuc-'+i1+'_'+c1+'-'+i2+'_'+c2+'.csv', 'w', newline='') as csvfile:
					spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
					
					spamwriter.writerow(['Créditos-aula por Núcleo'])
					spamwriter.writerow([course1.university, course1.name, course2.university, course2.name])
					spamwriter.writerow(list(course1.getDisciplineCount())) # núcles
					spamwriter.writerow(list(course1.getDisciplineCount().values()))	# créditos
					spamwriter.writerow(list(course2.getDisciplineCount().values()))	# créditos

				# Gerando imagem do gráfico de venn
				plt.plotVenn(course1, course2);
		
		# insera a instituição na lista das processadas para que não haja arquivos duplicados
		instProc.append(i1)

	
'''
	#gera um grafico
	plt.plotOneBar(icmc_bcc);
	plt.plotTwoBar(ufrgs, icmc_bcc);
	plt.plotVenn(ufrgs, icmc_bcc);
	plt.plotTextList(ufrgs,icmc_bcc);
'''