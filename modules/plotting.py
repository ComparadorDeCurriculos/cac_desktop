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
	plt.xticks(index+(barWidth/2),labels,size='small');

	plt.tight_layout();

	plt.savefig(name,bbox_inches='tight');

#generates a bar graph with the SBC cores as labels
def plotBarCores(name,values):
	labels = ('Fundamentos\nde\nComputação\n',
		'Tecnologias\nde\nComputação\n',
		'Matemática\n',
		'Ciências\nBásicas',
		'Eletrônica\n',
		'Contexto Social\ne\nProfissional\n');
	plotBar(name, labels, values, title='Créditos por Núcleo');