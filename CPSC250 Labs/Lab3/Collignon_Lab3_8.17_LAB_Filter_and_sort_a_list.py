num_list=input().split(" ")
for x in range(len(num_list)):
    num_list[x]=int(num_list[x])
new_list=[]
for x in num_list:
    if x<0:
        new_list.append(x)
new_list.sort(reverse=True)
for x in new_list:
    print(x,end=' ')