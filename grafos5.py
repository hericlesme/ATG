# coding: utf-8
# UFCG - Aplicações de Teoria dos Grafos - 2017.2
# Aluno: Héricles Emanuel - Matrícula: 117110647

# Gera um Grafo
dic = {}
cortes = []
n = int(input())
for i in range(n):
    vert = raw_input()
    ar = raw_input().split()
    dic[vert] = ar

# Recebe o conjunto de vértices

part = raw_input().split()

# Procura o conjunto de corte de arestas, e as separa na lista cortes

for i in part:
    string = i
    for e in range(len(dic[i])):
        if dic[i][e] not in part:
            string += dic[i][e]
    cortes.append(string)
    cortes.append(string[::-1])

# Imprime o corte de arestas
for i in sorted(cortes): print(i)
