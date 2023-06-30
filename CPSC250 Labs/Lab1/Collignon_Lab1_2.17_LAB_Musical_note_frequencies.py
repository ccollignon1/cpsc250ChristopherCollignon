import math
r=math.pow(2,1/12)
f0=int(input())
print(f'{f0:.2f} Hz')
f1=f0*math.pow(r,1)
print(f'{f1:.2f} Hz')
f2=f0*math.pow(r,2)
print(f'{f2:.2f} Hz')
f3=f0*math.pow(r,3)
print(f'{f3:.2f} Hz')


