from Course import *
import plotting as plt
import Discipline

if __name__ == '__main__':

	course1 = Course("BCC", "USP", "cursos/gradeBCC.txt")

	res = course1.getCoresCreditsDict()

	#### usa esse codigo pra printar o numero de creditos por nucleo
	# for value in res:
	# 	print("{0:s}: {1:d}".format(value, res[value]))
	# print()
	
	#### usa esse codigo pra printar as disciplinas de cada nucleo
	# for cores in Discipline.Discipline.sbcCores:
	# 	print(cores);
	# 	res = course1.getCoreDisciplines(cores)
	# 	for disc in res:
	# 		print(disc.name);
	# 	print();

	#gera um grafico 
	plt.plotBarCores('result.pdf',course1.getCoresCreditsList());