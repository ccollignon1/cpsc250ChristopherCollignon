import math
x=float(input())
y=float(input())
z=float(input())
num1=math.pow(x,z)
num2=math.pow(x,math.pow(y,z))
num3=math.fabs(x-y)
num4=math.sqrt(math.pow(x,z))

print(f'{num1:.2f} {num2:.2f} {num3:.2f} {num4:.2f}')

