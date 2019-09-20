n = int(input())
s = list(input())
k = int(input())
res= ''
for i in s:
    if i.isalpha():
        a = 'A' if i.isupper() else 'a'
        res+= chr(ord(a)+(ord(i)-ord(a)+k)%26)
    else:
        res+=i
print(res)