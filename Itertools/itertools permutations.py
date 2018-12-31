import itertools

s = input()
word = list(s[:s.index(" ")])
k = int(s[s.index(" "):])
perms = list(itertools.permutations(word,k))
perms.sort()
for w in perms:
    print("".join(w))