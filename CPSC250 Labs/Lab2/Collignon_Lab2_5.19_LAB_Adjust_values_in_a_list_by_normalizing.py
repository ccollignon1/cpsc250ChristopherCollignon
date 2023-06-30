num1=int(input())
num_list=[]
for x in range(num1):
    num_list.append(float(input()))
max1=max(num_list)
for y in range(len(num_list)):
    print(f'{num_list[y]/max1:.2f}')