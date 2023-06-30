# TODO: Write recursive print_num_pattern() function
def print_num_pattern(num1, num2):
    print(num1, end=' ')
    sub = num1 - num2
    if sub < 0:
        print(sub, end=' ')
    else:

        print_num_pattern(sub, num2)
    print(num1, end=' ')


if __name__ == "__main__":
    num1 = int(input())
    num2 = int(input())
    print_num_pattern(num1, num2)