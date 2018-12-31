import itertools

s = input()
word = list(s[:s.index(" ")])
word.sort()
k = int(s[s.index(" "):])
for i in range(1,k+1):
    perms = list(itertools.combinations(word,i))
    for w in perms:
        print("".join(w))