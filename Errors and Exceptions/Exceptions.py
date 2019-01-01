for i in range(int(input())):
    a = list(input().split())
    try:
        print (int(a[0])//int(a[1]))
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)

