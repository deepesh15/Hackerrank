import numpy
lst = list(map(float,input().split()))
val = float(input())
print(numpy.polyval(lst,val))