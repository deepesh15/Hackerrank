import numpy
numpy.set_printoptions(legacy = '1.13')
n,m = map(int,input().split())
lst = []
for _ in range(n):
    lst.append(list(map(int,input().strip().split())))

A = numpy.array(lst,float)

print(numpy.mean(A,axis=1))
print(numpy.var(A,axis=0))
print(numpy.std(A,axis=None))