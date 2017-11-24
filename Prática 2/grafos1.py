# coding: utf-8
# Aluno: Héricles Emanuel Gomes da Silva - 117110647
# Aplicacão de Teoria de grafos - Turma 02 - 2017.2

# Checa se o passeio dado na entrada é válido;
# Retorna um boolean indicando a validade do passeio.

def checaPasseio():
    checou = True
    for i in range(len(passeio)-1):
        if not passeio[i][1] == passeio[i+1][0]:
            checou = False
    return checou

# Checa se não existem arestas repetidas, ou seja, se o passeio é uma trilha.

def checaValido():
    for i in passeio:
        count = 0
        for e in passeio:
            if i == e[::-1] or i == e:
                count += 1
        if count > 1:
            return False
    return True

# Monta o grafo a partir dos vértices e arestas na entrada.
dic = {}
lista = []
n = int(raw_input())
for i in range(n):
	vert = raw_input()
	dic[vert] = raw_input().split()
passeio = raw_input().split()

print(checaPasseio() and checaValido())
