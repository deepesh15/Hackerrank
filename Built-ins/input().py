x,k = map(float,input().split())
eqn = str(input())
if(eval(eqn.replace("x",str(x))) == k):
    print("True")
else:
    print("False")