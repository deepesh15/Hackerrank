n = int(input())       
password = input()
count = 0
if any(l.isdigit() for l in password) == False:
    count+=1
if any(l.isupper() for l in password) == False:
    count+=1
if any(l.islower() for l in password) == False:
    count+=1
if any(l in '!@#$%^&*()-+' for l in password) == False:
    count+=1
print(max(count,6-n))