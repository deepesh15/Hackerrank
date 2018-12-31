import math
y1 = int(input())       #y co-ordiate of AB
x2 = int(input())       # x co-ordinate of BC
mx = x2/2               #mid x co-ordinate of hypotenuse AC
my = y1/2               #mid y co-ordinate of hypotenuse BC
dis_frm_orign = math.sqrt(mx**2+my**2)
rad_angle = math.degrees(math.atan(y1/x2))
angle = str(int(round(rad_angle)))+"°"
print(angle)