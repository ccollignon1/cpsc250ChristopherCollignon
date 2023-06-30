user_string = input()

try:
    user_int = int(user_string)
    if user_int > 0:
        print("Yes")
    else:
        print("No")

except:
    print("No")
