import sys


def loop_pow(mark_count, b):
    while pow(2, mark_count) <= b:
        if b % pow(2, mark_count) == 0:
            mark_count += 1
            loop_pow(mark_count, b)
        else:
            return mark_count
    return mark_count


def contract(digit):
    count = 1
    while pow(2, count) < digit:
        count += 1
    return pow(2, count - 1), pow(2, count + 1)


if __name__ == '__main__':
    b = 125
    count = 0
    while b != 1:
        if b % 2 == 0:
            b = b / 2
        else:
            c = b - 1
            if c == 2:
                b = c
                count += 1
                continue
            mark_count = 1
            minus = loop_pow(mark_count, c)
            d = b + 1
            plus = loop_pow(mark_count, d)
            if minus >= plus:
                b = c
            else:
                b = d
            count += 1
            b = b / 2
        count += 1
    print(count)