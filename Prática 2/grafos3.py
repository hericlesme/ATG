# coding: utf-8
# Aluno: Héricles Emanuel Gomes da Silva - 117110647
# Aplicacão de Teoria de grafos - Turma 02 - 2017.2

# Recebe um grafo, e separa suas arestas em uma lista;
# As arestas colocadas são no formato xy, yx;
# Visto que é possível ter vértices de entrada e saída inversos

def criaArestas(grafo):
	arestas = []
	for i in grafo:
		for e in grafo[i]:
			if i+e not in arestas:
				arestas.append(i+e)
			if e+i not in arestas:
				arestas.append(e+i)
	return arestas

# A partir da árvore geradora dada, por suas arestas, cria uma co-árvore e a retorna

def geraCoArvore():
	coArvore = []
	for i in arestas:
		if not (i in geradora or i[::-1] in geradora):
			coArvore.append(i)
	return sorted(coArvore)

# Monta o grafo a partir dos vértices e arestas na entrada.

dic = {}
n = int(raw_input())
for i in range(n):
	vert = raw_input()
	adj = raw_input().split()
	dic[vert] = adj

geradora = raw_input().split()
arestas = criaArestas(dic)
string = ""
for i in (geraCoArvore()):
	string += i + " "

print(string)
