import numpy
numpy.set_printoptions(legacy = '1.13')
n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(float,input().split())))

A =numpy.array(lst,float)
print(numpy.linalg.det(A))