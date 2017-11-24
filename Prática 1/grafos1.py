dic = {}
lista = []
n = int(raw_input())
for i in range(n):
	vert = raw_input()
	lig = raw_input().split()
	dic[vert] = lig
	
for e in dic:
	if dic[e] == []:
		lista.append(e)
print (lista)
