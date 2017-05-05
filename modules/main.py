from course import Course
import plotting as plt

if __name__ == '__main__':

	sbc = Course("Referência", "SBC", "nucleos/computacao_ref.txt")
	icmc = Course("BCC", "ICMC", "cursos/BCC_ICMC.txt", sbc)
	ime = Course("BCC", "IME", "cursos/BCC_IME.txt", sbc)

	#gera um grafico 
	plt.plotBarCores('result.pdf', icmc.getCoresCreditsDict());
	plt.plotBarCores('result2.pdf', ime.getCoresCreditsDict());

	plt.plotVenn(icmc.compare(ime, 0.15), "venn.pdf");