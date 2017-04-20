from course import Course
import plotting as plt

if __name__ == '__main__':

	sbc = Course("Referência", "SBC", "nucleos/computacao_ref.txt")
	icmc = Course("BCC", "ICMC", "cursos/gradeBCC.txt", sbc)

	#gera um grafico 
	plt.plotBarCores('result.pdf', icmc.getCoresCreditsDict());
	plt.plotBarCores('result2.pdf', sbc.getCoresCreditsDict());

	plt.plotVenn(icmc.compare(sbc, 0.15), "venn.pdf");