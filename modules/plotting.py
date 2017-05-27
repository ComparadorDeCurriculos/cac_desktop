import sys
from matplotlib import pyplot as plt
import numpy as np
from matplotlib_venn import venn2, venn2_circles

def titleize(text, exceptions):
    exceptions = exceptions.split()
    text = text.split()
    # Capitalize every word that is not on "exceptions" list
    for i, word in enumerate(text):
        text[i] = word.title() if word not in exceptions or i == 0 else word
    # Capitalize first word no matter what
    return ' '.join(text)

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

def removePlotBorders(fig, ax):
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


def _plotOneBar(name,labels,values,title):

	#removing borders
	fig, ax = plt.subplots();
	# removePlotBorders(fig,ax);

	barWidth = 0.7;
	index = np.arange(len(values));

	bars = ax.bar(index,values,barWidth,
		color='#0066cc',
		label='BCC',
		linewidth=0);

	autoLabel(ax,bars);
	plt.xlabel('Núcleos do curriculo de referência')
	plt.ylabel('Créditos-Aula')

	plt.title(title);
	plt.xticks(index,labels,size='small');

	plt.tight_layout();

	plt.savefig(name,bbox_inches='tight');

	plt.clf();

def _plotTwoBar(name,labels,name1,name2,val1,val2,title):

	fig, ax = plt.subplots();
	# removePlotBorders(fig,ax);

	barWidth = 0.35;
	index = np.arange(len(val1));

	bars1 = ax.bar(index,val1,barWidth,
		color='red',
		linewidth=0);
	bars2 = ax.bar(index+barWidth,val2,barWidth,
		color='#0066cc',
		linewidth=0);

	autoLabel(ax,bars1);
	autoLabel(ax,bars2);

	plt.xlabel('Núcleos do curriculo de referência')
	plt.ylabel('Créditos-Aula')

	plt.xticks(index+(barWidth/2.0),labels,size='small');

	plt.title(title);

	ax.legend((bars1[0], bars2[0]),(name1,name2),frameon=False, title="Cursos")

	plt.tight_layout();

	plt.savefig(name,bbox_inches='tight');
	plt.clf();

def setLabels(course):
	#alphabetically sorts labels
	oldlabels = []
	for core in course.cores:
		oldlabels.append(core);
	values = course.getCoresCreditsList();

	oldlabels, values = zip(*sorted(zip(oldlabels, values)))

	labels = []
	for label in oldlabels:
		labels.append(label.replace(' ','\n'));

	return (labels, values)

def plotOneBar(course):

	#sets filename
	filename = "results/" + course.university + "-" + course.name + ".png"

	name = course.university + ' ' + course.name

	#alphabetically sorts x-axis labels
	labels, values = setLabels(course)

	_plotOneBar(filename, labels, values, title='Créditos-aula por Núcleo\n{0}'.format(name))

def plotTwoBar(course1, course2):

	#sets filename
	filename = "results/" + course1.university + "-" + course1.name + '_' +  course2.university + '-' + course1.name + "_2bar.png"

	name1 = course1.university + ' ' + course1.name
	name2 = course2.university + ' ' + course2.name

	#alphabetically sorts x-axis labels.
	labels, val1 = setLabels(course1)
	print(labels);
	labels, val2 = setLabels(course2)
	print(labels);

	_plotTwoBar(filename, labels, name1, name2, val1, val2, title='Créditos-aula por Núcleo\n{0} x {1}'.format(name1,name2))

def plotVenn(course1,course2):
	"""plots a venn diagram with the result of a Course.compare()
	
	Args:
	    result (tuple): return of a Course.compare() call
	    filename (str): name of the resulting file
	"""

	filename = "results/" + course1.university + "-" + course1.name + '_' +  course2.university + '-' + course1.name + "_venn.png"
	result = course1.compare(course2,0.2);

	s = (len(result[0]),len(result[1]),len(result[2]))
	v = venn2(subsets=s, set_labels=(result[3][0],result[3][1]), set_colors=['red','#0066cc'], alpha=1.0);

	# Subset labels
	v.get_label_by_id('10').set_text(s[0])
	v.get_label_by_id('01').set_text(s[1])
	v.get_label_by_id('11').set_text(s[2])

	# Subset colors
	v.get_patch_by_id('10').set_color('red')
	v.get_patch_by_id('11').set_color('yellow')

	# Subset alphas
	v.get_patch_by_id('10').set_alpha(1.0)#0.4
	v.get_patch_by_id('01').set_alpha(1.0)#1.0
	v.get_patch_by_id('11').set_alpha(0.7)#0.7
	
	# Border styles
	c = venn2_circles(subsets=s, linestyle='solid')

	plt.legend(v.patches, (v.set_labels[0].get_text(),v.set_labels[1].get_text()),frameon=False)
	plt.title("Número de disciplinas equivalentes e únicas de cada curso");

	plt.tight_layout();

	plt.savefig(filename)
	plt.clf();

def plotTextList(course1,course2):
	"""Plots a list with disciplines compared through Course.compare()
	
	Args:
	    compResult (Tuple): the return of a Course.compare() call
	    filename (str): the name of the resulting file
	"""
	filename = "results/" + course1.university + "-" + course1.name + '_' +  course2.university + '-' + course1.name + "_text.png"
	compResult = course1.compare(course2,0.2);

	#finding bigger set of disciplines 
	nitens = 0; 
	for i in range(0,3): 
		if(len(compResult[i]) > nitens): 
			nitens = len(compResult[i])  

	# padding between boxes
	hpad = 0.2
	# starting position for boxes
	hbegin = 0.07;
	# height of the figure
	figheight = ((nitens+4)*hpad)+hbegin;
 	# font size
	fontsize = 0.35*14

	#setting the figure size
	fig1 = plt.figure(1, (4/1.5, (figheight/1.5)))

	#plot title
	fig1.text(0.5, 0.97,
		"Lista de disciplinas equivalentes e únicas entre os cursos",
		 size=fontsize*2, ha='center') 
	
	#for each subset (Ab, aB, AB), plots its disciplines
	for subset in range(0,3): 
		# Setting the correct 
		if (subset == 0): 
			courseName = compResult[3][0]
			ec = '#c62828'
			fc = 'red'
			x = 0.2 
		elif (subset == 2): 
			courseName = "Equivalentes"
			ec = '#c49000'
			fc = 'yellow'
			x = 0.5 
		elif (subset == 1): 
			courseName = compResult[3][1]
			ec = '#283593'
			fc = '#0066cc'
			x = 0.8 

		# plots the name of the course over the list of disciplines
		fig1.text(x, 0.93, courseName, size=fontsize*1.5, ha='center', wrap=True)

		for v, discipline in enumerate(compResult[subset]):
			# When fetching discipline name for the AB subset, the 'discipline' will be a tuple with two disciplines
			if type(discipline) is tuple: 
				discipline = discipline[1]

			# Use titleized case on text (This is an Example)
			usedWord = titleize(discipline.name.lower(),"à em de da a e")

			y = ((hpad * (nitens - v))/figheight)
			# plots each discipline
			fig1.text(x, y, usedWord, size=fontsize, ha='center', wrap=True, bbox=dict(boxstyle="round",fc=fc, ec=ec, alpha=0.6))

	plt.savefig(filename, dpi=200)
	plt.clf();

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