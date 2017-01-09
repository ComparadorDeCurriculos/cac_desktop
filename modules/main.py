import WordEmbedding;

teste = WordEmbedding.wordEmbedding('stoplist_portugues.txt','base_tep2.txt');
teste.addDoc('1.txt');
teste.addDoc('2.txt');

print(teste.compare('1.txt','2.txt'));