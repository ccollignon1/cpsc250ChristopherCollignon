''' Read in first equation, ax + by = c '''
a = int(input())
b = int(input())
c = int(input())

''' Read in second equation, dx + ey = f '''
d = int(input())
e = int(input())
f = int(input())

found = False
for x in range(-10, 11):
    for y in range(-10, 11):
        # print(a*x+b*y)
        # print(c)
        # print((a*x+b*y)==c)
        # print((d*x+e*y)==f)
        if (a * x + b * y) == c and (d * x + e * y) == f:
            found = True
            x_keep = x
            y_keep = y
            break

if found:
    print("x =", x_keep, ", y =", y_keep)
else:
    print("There is no solution")



