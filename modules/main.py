from Course import *


if __name__ == '__main__':

	begin = time.time()
	course1 = Course("BCC", "USP", "../gradeBCC.txt")
	end = time.time()
	time1 = end - begin

	begin = time.time()
	course2 = Course("BCC 2", "USP", "../gradeBSI.txt")
	end = time.time()
	time2 = end - begin

	print('Time to create course 1 {0:.2f}s'.format(time1))
	print('Time to create course 2 {0:.2f}s'.format(time2))
	print('compatibility {0:.2f}%'.format(100*course1.compare(course2)))