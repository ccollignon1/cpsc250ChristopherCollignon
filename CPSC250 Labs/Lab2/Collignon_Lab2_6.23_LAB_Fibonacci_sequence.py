def fibonacci(n):
    n1 = 0
    n2 = 1
    n_f = 0
    if n < 0:
        return (-1)
    else:

        for x in range(n):
            n_f = n1 + n2
            n1 = n2
            n2 = n_f

        return (n1)


if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')