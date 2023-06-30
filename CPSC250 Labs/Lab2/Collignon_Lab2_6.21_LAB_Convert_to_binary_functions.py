def int_to_reverse_binary(integer_value):
    # binary=format(integer_value,'b')
    # binary=binary[::-1]
    binary_str = ''
    while integer_value > 0:
        binary_str += str((integer_value % 2))
        integer_value = integer_value // 2

    return (binary_str)


def string_reverse(binary_string):
    binary_string = binary_string[::-1]
    return (binary_string)


if __name__ == '__main__':
    bin1 = int_to_reverse_binary(int(input()))
    bin2 = string_reverse(bin1)

    print(bin2)
    # Type your code here. 
    # Your code must call int_to_reverse_binary() to get 
    # the binary string of an integer in a reverse order.
    # Then call string_reverse() to reverse the string
    # returned from int_to_reverse_binary().

