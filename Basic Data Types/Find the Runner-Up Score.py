if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l = list(arr)
    #print(l)
    # creating a list with no repeated values
    nr_list =[]
    for i in l: 
        if i not in nr_list: 
            nr_list.append(i)

    #print("list>",l)
    #print("nr_list>",nr_list) 
    nr_list.remove(max(nr_list))
    print(max(nr_list))
            




'''
You cannot assign to a list like lst[i] = something, unless the list already is initialized with at least i+1 elements. 
You need to use append to add elements to the end of the list. lst.append(something).

https://stackoverflow.com/questions/10712002/create-an-empty-list-in-python-with-certain-size
'''


