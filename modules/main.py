from WordEmbedding import *

f1 = open('1.txt');
f2 = open('2.txt');

a = wordEmbedding(f1.read());
b = wordEmbedding(f2.read());

print(a.compare(b));