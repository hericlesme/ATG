# coding: utf-8
# Aluno: Héricles Emanuel Gomes da Silva - 117110647
# Aplicação de teoria dos grafos.

# Calcula a somatoria dos fluxos de saida.
def somatorioFluxos():
    f = 0
    for i in capacidade:
        if i[0] in corte:
            if i[1] not in corte:
                f += int(fluxo[i])
    return f

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

# Recebe os vértices do corte.
corte = input().split()

# Imprime a soma dos fluxos.
print(somatorioFluxos())