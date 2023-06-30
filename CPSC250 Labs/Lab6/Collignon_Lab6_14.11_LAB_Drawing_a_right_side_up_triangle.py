# TODO: Write recursive draw_triangle() function here.
def draw_triangle(base_length,symbol=1,space=9):
    if symbol>base_length:
        return
    else:
        print(' '*space + '*'*symbol)
        draw_triangle(base_length,symbol+2,space-1)


if __name__ == '__main__':
    base_length = int(input())
    draw_triangle(base_length)