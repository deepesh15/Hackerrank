s = list(input())
#lst  = [s.remove(s[i]) for i in range(0,len(s),1) if s[i-1] == s[i]]

i=0
while i < len(s)-1:
    if s[i] == s[i+1]:
        del s[i+1]
        del s[i]
        i=0
    else:
        i+=1

if len(s)>0:
    print(''.join(s))
else:
    print("Empty String")