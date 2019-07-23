t= int(input())
for _ in range(t):
    n = int(input())
    temp = n
    c=0
    while(temp>0):
        d = temp%10
        temp = temp//10
        if(d>0):
            if(n%d == 0):
                c+=1
    print(c)