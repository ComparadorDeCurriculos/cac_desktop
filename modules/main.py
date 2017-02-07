from Course import *
import Discipline

if __name__ == '__main__':

	course1 = Course("BCC", "USP", "gradeBCC.txt")

	res = course1.getCoresCredits()
	for value in res:
		print("{0:s}: {1:d}".format(value, res[value]))
	print()
	# print("Eletrônica")
	# res = course1.getCoreDisciplines('Eletrônica')
	# or disc in res:
	# 	print(disc.name);
	# print('\n');

	# print('Matemática')
	# res = course1.getCoreDisciplines('Matemática')
	# for disc in res:
	# 	print(disc.name);
	# print('\n')

	# print('Fundamentos de computação')
	# res = course1.getCoreDisciplines('Fundamentos de Computação')
	# for disc in res:
	# 	print(disc.name);
	# print('\n');


	# print('Tecnologias de computação')
	# res = course1.getCoreDisciplines('Tecnologias de Computação')
	# for disc in res:
	# 	print(disc.name);
	# print('\n');


	# print('')
	# res = course1.getCoreDisciplines('Tecnologias de Computação')
	# for disc in res:
	# 	print(disc.name);
	# print('\n');

	for cores in Discipline.Discipline.sbcCores:
		print(cores);
		res = course1.getCoreDisciplines(cores)
		for disc in res:
			print(disc.name);
		print();