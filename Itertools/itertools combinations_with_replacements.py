import itertools

s = input()
word = list(s[:s.index(" ")])
word.sort()
k = int(s[s.index(" "):])
perms = list(itertools.combinations_with_replacement(word,k))
for w in perms:
    print("".join(w))