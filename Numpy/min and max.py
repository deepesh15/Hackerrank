import numpy

n,m = map(int,input().split())
lst = []
for _ in range(n):
    lst.append(list(map(int,input().split())))
arr = numpy.array(lst)
result = numpy.min(arr,axis=1)
print(numpy.max(result))