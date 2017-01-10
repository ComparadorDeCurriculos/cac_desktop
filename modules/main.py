from WordEmbedding import *

f1 = open('1.txt');
f2 = open('2.txt');
f3 = open('nucleos/matematica.txt');
f4 = open('nucleos/profissional.txt')

a = wordEmbedding(f1.read());
b = wordEmbedding(f2.read());
c = wordEmbedding(f3.read());
d = wordEmbedding(f4.read());

print(c.compare(a));
print(d.compare(a));