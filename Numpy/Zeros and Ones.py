import numpy
a,b,c = map(int,input().split())
for _ in range(c):
    print(numpy.zeros((a,b), dtype = numpy.int))

for _ in range(c):
    print(numpy.ones((a,b), dtype = numpy.int))
    
