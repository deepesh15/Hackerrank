import collections

o_dic = collections.OrderedDict()
for i in range(int(input())):
    inpt = str(input())
    item_name,net_price =  str(inpt[:inpt.index(" ")]),int(inpt[inpt.index(" "):])
    o_dic[item_name] = net_price
new_set = set(o_dic)
print(new_set)