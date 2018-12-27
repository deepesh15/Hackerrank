
# Complete the solve function below.
def solve(s):
    for x in s[:].split():
        s = s.replace(x,x.capitalize())
    
    return s

if __name__ == '__main__':

    s = input()
    solve(s)
    result = solve(s)
    print(result)

