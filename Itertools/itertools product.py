import itertools

lst_a = list(map(int,input().split()))
lst_b = list(map(int,input().split()))
cart_prod = list(itertools.product(lst_a,lst_b))
for each in cart_prod:
    print(each,end =" ")
