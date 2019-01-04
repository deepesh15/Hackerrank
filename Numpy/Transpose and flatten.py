import numpy
n,m = map(int,input().split())
lst = []
for _ in range(n):
    lst.append(list(map(int,input().strip().split(' '))))
arr = numpy.array(lst)
print(numpy.transpose(arr))
print(arr.flatten())