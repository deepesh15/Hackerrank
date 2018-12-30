size = int(input())
room_list = list(map(int,input().split()))
#print("room_list    : ",room_list)
for i in range(len(room_list)):
    j = 0
    while(j<len(room_list)):
        if(i != j and room_list[i] == room_list[j]):
            break
        j +=1
        if(j==len(room_list)):
            print(room_list[i])
        