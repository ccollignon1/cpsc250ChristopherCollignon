num_list = input().split(' ')
for x in range(len(num_list)):
    num_list[x] = float(num_list[x])

max_num = max(num_list)
avg_num = sum(num_list) / len(num_list)
print(f'{max_num:.2f} {avg_num:.2f}')