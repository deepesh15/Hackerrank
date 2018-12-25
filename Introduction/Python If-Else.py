N = int(input())

if(N%2 == 1):
    print("Weird")

if (N % 2 == 0):
    if N >20 or (N>2 and N<5):
        print("Not Weird")
    else:
        print("Weird")