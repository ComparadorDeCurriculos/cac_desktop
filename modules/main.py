from course import Course
import plotting as plt

if __name__ == '__main__':

	sbc = Course("Referência", "SBC", "nucleos/computacao_ref.txt")
	icmc_bcc = Course("BCC", "ICMC", "cursos/BCC_ICMC.txt", sbc)
	# icmc_bsi = Course("BSI", "ICMC", "cursos/BSI_ICMC.txt", sbc)
	ime = Course("BCC", "IME", "cursos/BCC_IME.txt", sbc)
	ufrgs = Course("BCC", "UFRGS", "cursos/BCC_UFRGS.txt", sbc)

	#gera um grafico 
	plt.plotBarCores('bar_icmc_bcc.pdf', icmc_bcc.getCoresCreditsDict());
	# plt.plotBarCores('bar_icmc_bsi.pdf', icmc_bsi.getCoresCreditsDict());
	plt.plotBarCores('bar_ime_bcc.pdf', ime.getCoresCreditsDict());
	plt.plotBarCores('bar_ufrgs_bcc.pdf', ufrgs.getCoresCreditsDict());

	result1 = icmc_bcc.compare(ime, 0.15)
	plt.printComparisson(result1 , file=open('icmc_bccXime.txt',mode='x'))
	plt.plotTextList(result1,"icmc_bccXime_list.pdf");
	result2 = icmc_bcc.compare(ufrgs, 0.15)
	plt.printComparisson(result1 , file=open('icmc_bccXufrgs.txt',mode='x'))
	plt.plotTextList(result1,"icmc_bccXufrgs_list.pdf");

	plt.plotVenn(result1 , "icmc_bccXime.pdf");
	plt.plotVenn(result2, "icmc_bccXufrgs.pdf");
