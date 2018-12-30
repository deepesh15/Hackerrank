k, arr = int(input()),list(map(int,input().split()))
room_set = set(arr)
print((((sum(room_set))*k - sum(arr))//(k-1)))