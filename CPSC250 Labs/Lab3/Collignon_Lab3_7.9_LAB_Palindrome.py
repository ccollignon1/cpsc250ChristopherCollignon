string_in = input()
string = string_in.replace(' ', '')
check = False
for x in range(len(string) // 2):

    if string[x] == string[-x - 1]:
        check = True
    else:
        check = False
        break
if check:
    print("palindrome:", string_in)
else:
    print("not a palindrome:", string_in)