import WordEmbedding;

teste = WordEmbedding.wordEmbedding('stoplist_portugues.txt');
teste.addDoc('1.txt');
teste.addDoc('2.txt');
teste.compare('1.txt','2.txt');


print(teste.compare('1.txt','2.txt'));

print("teste de wordnet");

teste2 = WordEmbedding.wordNet('base_tep2.txt');

print(teste2.checkSynonym('absolver', 'isentar'));