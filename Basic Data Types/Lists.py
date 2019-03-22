lst = []
for _ in range(int(input())):
    text = input().split()
    cmd = text[0]
    para = text[1:]
    if cmd != 'print':
        cmd += "("+",".join(para)+"+"
        eval("lst."+cmd)
    else:
        print lst
'''

n = input()
l = []
for _ in range(n):
    s = raw_input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"
        eval("l."+cmd)
    else:
        print l
'''