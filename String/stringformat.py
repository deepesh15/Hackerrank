def print_formatted(number):
    wid = len("{0:b}".format(n))
    for i in range(1,number+1):
        print("{0:{wid}d} {0:{wid}o} {0:{wid}X} {0:{wid}b}".format(i,wid=wid))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)