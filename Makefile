
all:
	@python modules/main.py 
	@# @evince icmc_bccXime_list.pdf &
clear:
	rm *.pdf  -f
	rm *X*.txt -f
	rm bar*.pdf -f
	rm A*.txt B*.txt -f
