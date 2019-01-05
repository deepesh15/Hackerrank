import numpy

n = int(input())
lstA = []
lstB = []
for _ in range(n):
    lstA.append(list(map(int,input().split())))

for _ in range(n):
    lstB.append(list(map(int,input().split())))

A = numpy.array(lstA)
B = numpy.array(lstB)
print(A.dot(B))