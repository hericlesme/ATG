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

# Verifica se o passeio dado é uma trilha de Euler, conforme o conceito da questão
# Sendo sempre o passeio dado, válido, verificamos se ele percorre todas as arestas do grafo.

def verificaTrilha():
    for i in arestas:
        if not (i in passeio or i[::-1] in passeio):
            return False
    return True

# Monta o grafo a partir dos vértices e arestas na entrada.

dic = {}
n = int(raw_input())
for i in range(n):
    vert = raw_input()
    adj = raw_input().split()
    dic[vert] = adj

passeio = raw_input().split()
arestas = criaArestas(dic)
print(verificaTrilha())
