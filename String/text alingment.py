#Replace all ______ with rjust, ljust or center. 

t = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(t):
    print((c*i).rjust(t-1)+c+(c*i).ljust(t-1))

#Top Pillars
for i in range(t+1):
    print((c*t).center(t*2)+(c*t).center(t*6))

#Middle Belt
for i in range((t+1)//2):
    print((c*t*5).center(t*6))    

#Bottom Pillars
for i in range(t+1):
    print((c*t).center(t*2)+(c*t).center(t*6))    

#Bottom Cone
for i in range(t):
    print(((c*(t-i-1)).rjust(t)+c+(c*(t-i-1)).ljust(t)).rjust(t*6))

