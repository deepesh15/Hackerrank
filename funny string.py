s = list(input())
asc_num = [abs(ord(s[i]) - ord(s[i+1])) for i in range(0,len(s)-1,1)]
rev_asc_num = [abs(ord(s[i]) - ord(s[i-1])) for i in range(len(s)-1,0,-1)]
if asc_num == rev_asc_num:
    print("Funny")
else:
    print("Not Funny")


