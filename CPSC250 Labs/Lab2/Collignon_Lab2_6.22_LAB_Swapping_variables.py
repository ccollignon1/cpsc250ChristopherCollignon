def swap_values(i1, i2, i3, i4):
    i_return = [i2, i1, i4, i3]
    i_str = ''
    for x in range(len(i_return)):
        if x != 3:
            i_str += str(i_return[x]) + ' '
        else:
            i_str += str(i_return[x])

    # return(str(i2),str(i1),str(i4),str(i3))
    # return(i_str)
    return (i2, i1, i4, i3)


if __name__ == '__main__':
    # Type your code here. Your code must call the function.
    # print(swap_values(int(input()),int(input()),int(input()),int(input())))
    [int1, int2, int3, int4] = swap_values(int(input()), int(input()), int(input()), int(input()))
    print(int1, int2, int3, int4)