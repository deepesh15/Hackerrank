def average(array):
    array = set(array)
    tot = len(array)
    return (sum(array)/tot)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr= set(arr)
    result = average(arr)
    print(result)