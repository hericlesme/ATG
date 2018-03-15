# coding: utf-8
# Aluno: Héricles Emanuel Gomes da Silva - 117110647
# Aplicação de teoria dos grafos.

# Verifica a validade do fluxo.
def validaFluxo(origem,destino):
   entrada = 0
   saida = 0
   for i in capacidade:
        if i[1] != destino:
            for e in capacidade:
                if i[1] == e[1]:
                    entrada += int(fluxo[e])
            for k in capacidade:
                if i[1] == k[0]:
                    saida += int(fluxo[k])
        if entrada != saida:
            return False
   return True

# Gera um dígrafo a partir do número de vértices passados, e a entrada que será dada em sua execução.
def geraGrafo(n):
    dic = {}
    for i in range(n):
        vert = input()
        adj = input().split()
        for e in range(len(adj)):
            if e % 2 == 0:
                dic[vert + adj[e]] = adj[e + 1]
    return dic

# Recebe o número de vértices dos dígrafos.
n = int(input())

# Chama o método geraGrafo, e cria um dígrafo com as capacidades de fluxo para cada arco.
capacidade = geraGrafo(n)

# Chama o método geraGrafo, e cria um dígrafo com a quantidade de fluxo para cada arco.
fluxo = geraGrafo(n)

# Recebe a origem e o destino..
origem = raw_input()
destino = raw_input()

# Imprime a validade do fluxo.
print(validaFluxo(origem, destino))