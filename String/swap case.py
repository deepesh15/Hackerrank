def swap_case(s):
    lst = list(s)
    print(lst)
    for i in range(0,len(lst)):
        if lst[i].isupper() :
            lst[i] = lst[i].lower()
        else :
            lst[i] = lst[i].upper()
    s = "".join(lst)
    #print(lst)
    #print(s)
    return s

