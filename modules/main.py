from Course import *
import Discipline

if __name__ == '__main__':

	course1 = Course("BCC", "USP", "gradeBCC.txt")

	res = course1.getCoresCredits()
	for value in res:
		print("{0:s}: {1:d}".format(value, res[value]))
	print()
	
	for cores in Discipline.Discipline.sbcCores:
		print(cores);
		res = course1.getCoreDisciplines(cores)
		for disc in res:
			print(disc.name);
		print();

	