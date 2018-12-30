lst = []
for _ in range(int(input())):
    #eval('lst.{0}({1})'.format(*input().split()+['']+['']))
    text = input().split()
    cmd = text[0]
    para = text[1:]
    eval('lst.{0}({1})'.format(cmd,para))

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