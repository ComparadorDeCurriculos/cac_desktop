from course import Course
import plotting as plt

if __name__ == '__main__':

	sbc = Course("Referência", "SBC", "nucleos/computacao_ref.txt")
	icmc_bcc = Course("BCC", "ICMC", "cursos/BCC_ICMC.txt", sbc)
	ufrgs = Course("BCC", "UFRGS", "cursos/BCC_UFRGS.txt", sbc)

	#gera um grafico
	plt.plotOneBar(icmc_bcc);
	plt.plotTwoBar(ufrgs, icmc_bcc);
	plt.plotVenn(ufrgs, icmc_bcc);
	plt.plotTextList(ufrgs,icmc_bcc);
