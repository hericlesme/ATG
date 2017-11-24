# coding: utf-8
# UFCG - Aplicações de Teoria dos Grafos - 2017.2
# Aluno: Héricles Emanuel - Matrícula: 117110647

G = {}
S = {}
count = 0

# Verifica a existencia de vértices e arestas do grafo S no grafo G

def verifica():
	for i in S.keys():
		if i not in G.keys():
			return False
		else:
			for e in S[i]:
				if not e in G[i]:
					return False
	return True

# Gera um Grafo G a partir dos vértices e arestas dados na entrada

n = int(raw_input())
for i in range(n):
    vert = raw_input()
    ar = raw_input().split()
    G[vert] = ar

# Gera um possível subgrafo S a partir dos vértices e arestas dados na entrada

n = int(raw_input())
for i in range(n):
    vert = raw_input()
    ar = raw_input().split()
    S[vert] = ar

# Imprime o Valor da função que verifica se S é um subgrafo de G
print(verifica())
