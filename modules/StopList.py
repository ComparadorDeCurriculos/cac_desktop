class stoplist:

	def __init__(self, StopListFile):
		self.words = [];
		self.file = open(StopListFile);

		#gets file end
		self.file.seek(0,2);
		end = self.file.tell();
		self.file.seek(0,0);

		i = 0;
		#reads every line of the file
		while(self.file.tell() != end):
			#fetches each line
			text = self.file.readline().rstrip();
			#appends it to a vector of words
			self.words.append(text);
			++i;

		#creates a set of words
		self.words = set(self.words);

	def check(self, word):
		return word in self.words;


class wordEmbedding:

	def __init__(self,stoplistFilename):

		import Stemmer

		self.stemmer = Stemmer.Stemmer('portuguese');
		self.docs = {};
		self.words = {};
		self.embeddings = [];

		#generates required stopList, open docs
		self.stopList = stoplist(stoplistFilename);

	def addDoc(self,filename):

		import string

		try:
			newDoc = open(filename);
		except FileNotFoundError:
			print(filename, "not found");
			return;


		if newDoc.name not in self.docs:
				self.docs[newDoc.name] = newDoc;

		#reads text
		text = newDoc.read();
		#puts to lower case
		text = text.lower();
		#removing punctuation
		translator = str.maketrans({key:None for key in string.punctuation});
		text = text.translate(translator);
		#split words of text
		split_text = text.split();

		#stemming text
		stemmed_text = [];
		for word in split_text:
				stemmed_text.append(self.stemmer.stemWord(word));

		final_words = [];
		#removing stopwords
		for word in stemmed_text:
			if(not self.stopList.check(word)):
				final_words.append(word);

		self.words[newDoc.name] = final_words;

	def compare(self,doc1Filename,doc2Filename):

		#bag of words
		bow = [];

		#fetching doc1 words
		try:
			words1 = self.words[doc1Filename];
		except KeyError:
			print(doc1Filename,'not added to the program yet');
			return;

		#fetching doc2 words
		try:
			words2 = self.words[doc2Filename];
		except KeyError:
			print(doc2Filename,'not added to the program yet');
			return;

		#preparing bag of words
		for word in words1:
			if not (word in bow):
				bow.append(word);

		for word in words2:
			if not (word in bow):
				bow.append(word);

		#bag of words ready, preparing embedding
		embeddings = [bow,[0]*len(bow),[0]*len(bow)]
		#counting 
		for word in words1:
			if word in bow:
				embeddings[1][bow.index(word)] += 1;
		for word in words2:
			if word in bow:
				embeddings[2][bow.index(word)] += 1;

		#print('{0:13} | {1:5} | {2:5}|'.format('Bag of Words',' doc1',' doc2'))
		#for j in range(0, len(bow)):
		#	print('{0:13} | {1:5d} | {2:5d}|'.format(embeddings[0][j], embeddings[1][j], embeddings[2][j]))

		#calculating cosine between embeddings
		num = 0.0;
		den1 = 0.0;
		den2 = 0.0;
		
		for i, j in zip(embeddings[1],embeddings[2]):
			num += embeddings[1][i]*embeddings[2][j];
			den1 += embeddings[1][i]**2;
			den2 += embeddings[2][i]**2;

		den1 **= 0.5;
		den2 **= 0.5;

		res = num/(den1/den2);

		return res;