s,t = list(map(int,input().split()))
a,b = list(map(int,input().split()))
m,n = list(map(int,input().split()))
apples_loc = list(map(int,input().split()))
oranges_loc = list(map(int,input().split()))
for i in range(m):
    apples_loc[i] +=a
for i in range(n):
    oranges_loc[i] +=b
count_a,count_b = 0,0
for apple in apples_loc:
    if apple  in range(s,t+1):
        count_a+=1
print(count_a)
for orange in oranges_loc:
    if orange  in range(s,t+1):
        count_b+=1
print(count_b)

'''
really cool answer
print(sum([1 for x in apple if (x + a) >= s and (x + a) <= t]))
print(sum([1 for x in orange if (x + b) >= s and (x + b) <= t]))
'''