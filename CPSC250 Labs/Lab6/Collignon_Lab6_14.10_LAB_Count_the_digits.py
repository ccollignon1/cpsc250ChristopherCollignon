# TODO: Write recursive digit_count() function here.
def digit_count(num):
    if num<10:
        return 1
    else:
        return 1 + digit_count(num/10)
if __name__ == '__main__':
    num = int(input())
    digit = digit_count(num)
    print(digit)