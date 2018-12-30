n = int(input())
n_set = set(map(int,input().split()))
print("n set    :",n_set)
N = int(input())
for _ in range(0,N):
    eval('n_set.{0}({1})'.format(*input().split()+['']))

print(sum(n_set))