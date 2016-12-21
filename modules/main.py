import StopList;

teste = StopList.wordEmbedding('stoplist_portugues.txt');
teste.addDoc('1.txt');
teste.addDoc('2.txt');
teste.compare('1.txt','2.txt');


print(teste.compare('1.txt','2.txt'));