n_e = int(input())          #number of subscribers for english
e = set(input().split())
n_f = int(input())          ##number of subscribers for french
f = set(input().split())
count = 0
for i in e.intersection(f):
    count +=1
print(count)


