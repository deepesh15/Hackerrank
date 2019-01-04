import numpy
n = int(input())
lst = []
for _ in range(n):
    lst.append(numpy.array(map(float,input().split())))

print(lst)
print(numpy.linalg.det(lst))