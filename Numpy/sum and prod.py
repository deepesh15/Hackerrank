import numpy

n,m = map(int,input().split())
lst =[]
for _ in range(n):
    lst.append(list(map(int,input().split())))

arr = numpy.array(lst)

result = numpy.sum(arr, axis = 0)

print(numpy.product(result))