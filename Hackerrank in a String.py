n  = int(input())
s = str(input())
count =0
for l in 'hackerrank':
    if l in s[count:]:
        count =s.index(l,count)+1
    else:
        print("NO")
print("YES")