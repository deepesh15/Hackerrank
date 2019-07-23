n,t = map(int,input().split()) # n and t , where n denotes the number of width measurements you will receive and t the number of test cases
width = list(map(int,input().split()))
min_wid =[]
for k in range(t):
    i,j = map(int,input().split())
    lane = width[i:j+1]
    min_wid.append(min(lane))

for l in min_wid:
    print(l)