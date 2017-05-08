## Processamento Automático de Currículos de Cursos de Computação no Brasil

Este é um projeto de Cultura e Extensão, financiado pelo Programa Unificado de Bolsas (PuB) da Universidade de São Paulo (USP). Nele propõe-se a comparação automática de currículos de cursos de Computação no Brasil, utilizando técnicas de Processamento de Linguagem Natural. Buscamos desenvolver um software que possa auxiliar pré-vestibulandos a escolherem melhor sua graduação, visto que, para grande parte desse publico a diferença entre os cursos não é obtida trivialmente.


# Pré-requisitos 
Python 3.x
Página Oficial: https://www.python.org/
GitHub: https://github.com/python/cpython

PyStemmer 1.3.0 (ou superior)
Página Oficial: https://pypi.python.org/pypi/PyStemmer
GitHub: https://github.com/snowballstem/pystemmer

Matplotlib 2.0.0 (ou superior)
Página Oficial: http://matplotlib.org/
GitHub: https://github.com/matplotlib/matplotlib

Matplotlib-Venn 0.11.5 (ou superior)
Página Oficial: https://pypi.python.org/pypi/matplotlib-venn
GitHub: https://github.com/konstantint/matplotlib-venn


# Instalação 
Certifique-se de que todos os pré-requisitos estão devidamente instalados em seu computador e faça o download do projeto. Abra o terminal no diretório raiz e digite:

$ make test-install

Os arquivos "result.pdf" e "venn.pdf" irão aparecer na raiz e a saída do terminal deve ser a mensagem: "Tudo está funcionando bem". 

# Execução
Usamos um Makefile para executar o programam, portanto basta abrir um terminal na pasta raiz do projeto e executar:

$ make

# Autores 
Bruno Henrique Rasteiro - brunorasteiro96@gamil.com
Rafael Monteiro - rafaelmonteiro95@gmail.com
