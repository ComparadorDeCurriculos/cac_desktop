from Course import *
import plotting as plt
import Discipline as dp

if __name__ == '__main__':

	course1 = Course("BCC", "USP", "cursos/gradeBCC.txt")

	#### usa esse codigo pra printar o numero de creditos por nucleo
	#for value in res:
	#	print("{0:s}: {1:d}".format(value, res[value]))
	#print()
	
	#### usa esse codigo pra printar as disciplinas de cada nucleo
	for core in dp.Discipline.sbcCores:
		print('{0} => {1}'.format(core, course1.cores[core].credits))
		res = course1.getCoreDisciplines(core)
		for disc in res:
			print('- {0}'.format(disc.name))
		print()
	
	#gera um grafico 
	plt.plotBarCores('result.pdf', course1.getCoresCreditsDict());