all:
	@mkdir results -p
	@python modules/main.py 
clear:
	rm results/* -f
	rm *.pdf  -f
	rm *X*.txt -f
	rm bar*.pdf -f
	rm A*.txt B*.txt -f
