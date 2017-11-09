dic = {}
n = int(raw_input())
for i in range(n):
    vert = raw_input()
    ar = raw_input().split()
    dic[vert] = ar
anl = raw_input()
print (len(dic[anl]) + dic[anl].count(anl))
