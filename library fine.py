d1,m1,y1 = list(map(int,input().split()))                       #date on which the book was returned
d2,m2,y2 = list(map(int,input().split()))                       #date on which the book was due to be returned
fine =0
if y1>y2:
    fine = 10000
elif y1<=y2:
    if m1>m2 and (y1>=y2):
        fine = 500 * (m1-m2)
    elif m1<=m2:
        if (d1>d2 and (m1-m2>=0) and (y1>=y2)):
            fine = 15*(d1-d2)
        else:
            fine = 0
print(fine)