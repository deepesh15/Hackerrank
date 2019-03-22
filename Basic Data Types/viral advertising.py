n= int(input())
shared =5
liked = shared//2
tot_likes = liked
for _ in range(n-1):
    shared = liked*3
    liked =shared//2
    tot_likes += liked

print(tot_likes)