'''
q = int(input())
for _ in range(q):
    s = input()
    print(len(s)-len(set(s)))
'''
n = int(input())
for _ in range(n):
    count = 0
    word = input()
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            count += 1
    print(count)