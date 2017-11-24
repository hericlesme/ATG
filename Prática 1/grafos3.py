# coding: utf-8
# UFCG - Aplicações de Teoria dos Grafos - 2017.2
# Aluno: Héricles Emanuel - Matrícula: 117110647

# Gera um grafo

dic = {}
count = 0
n = int(raw_input())
for i in range(n):
    vert = raw_input()
    ar = raw_input().split()
    dic[vert] = ar

# Verifica se a quantidade de arestas adjascentes a um vértice 
# é maior ou igual que a quantidade de demais vértices

for k in dic.keys():
    if len(dic[k]) >= n - 1:
        count += 1
if count >= n:
    print(True)
else:
    print(False)
    