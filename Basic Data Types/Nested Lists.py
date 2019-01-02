marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))





''''
if __name__ == '__main__':
    n_list = []
    for _ in range(0,int(input())):
        n_list.append([input(),float(input())])
    
    sorted(n_list, key = n_list[0][1])
    print(n_list)
    
    #sprint(student_marks)


'''''