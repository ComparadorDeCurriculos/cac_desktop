all:
	@mkdir results -p
	@python3.5 modules/main.py 
clear:
	rm *.pdf  -f
	rm *X*.txt -f
	rm bar*.pdf -f
	rm A*.txt B*.txt -f
