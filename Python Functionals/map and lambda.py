cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    lst = []
    num=0
    pnum =1
    for _ in range(n):
        lst.append(num)
        sums = num + pnum
        pnum = num
        num =sums
    return lst

    # return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))