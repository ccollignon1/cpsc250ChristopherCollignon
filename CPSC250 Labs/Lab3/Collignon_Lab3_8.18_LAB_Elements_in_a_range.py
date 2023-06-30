num_list=input().split(' ')
num_list=[int(x) for x in num_list]
bounds=input().split(' ')
bounds=[int(x) for x in bounds]
for x in num_list:
    if x>=bounds[0] and x<=bounds[1]:
        print(x,end=',')