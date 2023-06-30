name=input()
name=name.split(" ")
if len(name)==2:
    print(name[1] + ", " + name[0][0] + '.')
else:
    print(name[2] + ', ' + name[0][0] + '.' + name[1][0] + '.')