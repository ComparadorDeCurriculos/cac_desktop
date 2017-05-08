import sys

def autoLabel(axis,rects):

	for rect in rects:
		height = rect.get_height();
		if(height < 4):
			text_height = height;
			clr = 'black';
		else:
			text_height = height-3;
			clr = 'white';

		axis.text(
			rect.get_x() + rect.get_width()/2.,
			text_height,
			'%d' % int(height),
			ha='center',
			va='bottom',
			color=clr);

def plotBar(name,labels,values,title):

	import matplotlib
	#changes matplotlib backend to one that isn't interactive
	#we don't need interactivity; we can just generate the image
	matplotlib.use('Agg');
	import matplotlib.pyplot as plt
	import numpy as np

	#removing borders
	fig, ax = plt.subplots();
	ax.spines['top'].set_visible(False);
	ax.spines['right'].set_visible(False);
	ax.spines['left'].set_visible(False);
	ax.spines['bottom'].set_visible(False);
	plt.tick_params(
		axis='x',
		which='both',
		bottom='off',
		top='off');
	plt.xticks([]);
	plt.yticks([]);

	barWidth = 0.7;
	index = np.arange(len(values));

	bars = ax.bar(index,values,barWidth,
		color='#0066cc',
		label='BCC',
		linewidth=0);

	autoLabel(ax,bars);

	plt.title(title);
	plt.xticks(index,labels,size='small');

	plt.tight_layout();

	plt.savefig(name,bbox_inches='tight');

	plt.clf();

# generates a bar graph with the SBC cores as labels
def plotBarCores(name, dicti):
	labels = ['Fundamentos\nde\nComputação\n', 
			  'Tecnologias\nde\nComputação\n',
			   'Matemática\n', 
			   'Ciências\nBásicas', 
			   'Eletrônica\n',
			   'Contexto Social\ne\nProfissional\n']
	values = [0, 1, 2, 3, 4, 5]

	# Filling in list values
	for core in dicti:
		if   (core == 'Fundamentos de Computação'):
			i = 0
		elif (core == 'Tecnologias de Computação'):
			i = 1
		elif (core == 'Matemática'):
			i = 2
		elif (core == 'Ciências Básicas'):
			i = 3
		elif (core == 'Eletrônica'):
			i = 4
		else:
			i = 5

		values[i] = dicti[core]

	plotBar(name, labels, values, title='Créditos por Núcleo ' + name.split('_')[1])


def plotVenn(result, filename):
	from matplotlib import pyplot as plt
	from matplotlib_venn import venn2, venn2_circles

	s = (len(result[0]),len(result[1]),len(result[2]))

	v = venn2(subsets=s, set_labels=result[3]);

	# Subset labels
	v.get_label_by_id('10').set_text(s[0])
	v.get_label_by_id('01').set_text(s[1])
	v.get_label_by_id('11').set_text(s[2])

	# Subset colors
	v.get_patch_by_id('10').set_color('red')#993333
	v.get_patch_by_id('01').set_color('blue')
	v.get_patch_by_id('11').set_color('c')

	# Subset alphas
	v.get_patch_by_id('10').set_alpha(0.8)#0.4
	v.get_patch_by_id('01').set_alpha(1.0)#1.0
	v.get_patch_by_id('11').set_alpha(0.8)#0.7

	# Border styles
	c = venn2_circles(subsets=s, linestyle='solid')
	c[0].set_ls('dashed')  # Line style
	c[0].set_lw(2.0)       # Line width

	plt.savefig(filename)
	plt.clf();

def plotTextList(compResult, filename):
	from matplotlib import pyplot as plt

	#finding bigger set of disciplines
	nitens = 0;
	for i in range(0,3):
		if(len(compResult[i]) > nitens):
			nitens = len(compResult[i]) 

	for i in range(0,3):
		if (i == 0):
			ha = 'left'
			ec = (1., 0.5, 0.5)
			fc = (1., 0.8, 0.8)
			x = 0.2
		elif (i == 1):
			ha = 'center'
			ec = (0.5, 1., 0.5)
			fc = (0.8, 1., 0.8)
			x = 0.5
		elif (i == 2):
			ha = 'right'
			ec = (0.5, 0.5, 1.)
			fc = (0.8, 0.8, 1.)
			x = 0.8

		hspacing = 0.2

		figheight = nitens*hspacing;

		fig1 = plt.figure(1, (4/1.5, figheight/1.5))

		fontsize = 0.3*14

		for v, word in enumerate(compResult[i]):
			if type(word) is tuple:
				word = word[1]
			fig1.text(x, (hspacing * (float(nitens) - v) - 0.5)/figheight, word, size=fontsize,
			 ha='center', wrap=True,
						bbox=dict(boxstyle="round",
	                   				ec=ec,
	                   				fc=fc,
	                   		   ))

	plt.savefig(filename);
	plt.clf()

def printComparisson(result, file=sys.stdout):

	equivalents = result[2]
	# ordenando
	i = 0
	while i < len(equivalents) :
		k = i
		maior = 0
		while k < len(equivalents) :
			if (equivalents[k][0] > maior) :
				maior = equivalents[k][0]
				temp = equivalents.pop(k)
				equivalents.insert(i, temp)
			k += 1
		i += 1

	#printando 
	for eq in equivalents:
		print('{0:.2f} => {1} <-> {2}'.format(eq[0], eq[1].name, eq[2].name), file=file)

def dumpCompResult(result, path):
	a_course_name = result[3][0].split(' ')[0]
	b_course_name = result[3][1].split(' ')[0]
	a_univ_name = result[3][0].split(' ')[1]
	b_univ_name = result[3][1].split(' ')[1]

	filename = path + a_course_name+"_"+a_univ_name+"_x_" + b_course_name+"_"+b_univ_name

	Afile = open("A_"+filename+".txt",mode='w')
	Bfile = open("B_"+filename+".txt",mode='w')
	ABfile = open("AB_"+filename+".txt",mode='w')

	#dumping A:
	for discipline in result[0]:
		print(discipline.name,file=Afile)

	#dumping B:
	for discipline in result[1]:
		print(discipline.name,file=Bfile)

	#dumping AB:
	for discipline_tuple in result[2]:
		print("{0} ; {1} ; [{2:.2%}]".format(discipline_tuple[1].name,
											discipline_tuple[2].name,
											discipline_tuple[0]), 
											file=ABfile)