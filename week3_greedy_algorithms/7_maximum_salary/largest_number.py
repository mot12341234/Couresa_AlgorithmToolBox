#Uses python3

import sys

def IsGreatOrEqual(max_digit, digit):
    # max_digit = 23
    # digit = 3
    # 323 and 233, then max_digit = 3
    return int(str(digit) + str(max_digit)) >= int(str(max_digit) + str(digit))


def largest_number(a):
    # res = ""
    # for x in a:
    #     res += x
    # return res

    res = []

    while a != []:
        max_digit = 0
        for digit in a:
            if IsGreatOrEqual(max_digit, digit):
                max_digit = digit
        res.append(max_digit)
        a.remove(max_digit)

    return res


if __name__ == '__main__':
    # input = sys.stdin.read()
    n = int(input())
    data = list(map(int, input().split()))
    print(''.join([str(i) for i in largest_number(data)]))
