# Uses python3
import sys


def get_change(m):
    # write your code here
    num_10 = m // 10
    num_5 = (m - num_10 * 10) // 5
    num_1 = m - num_10 * 10 - num_5 * 5

    total_num = num_10 + num_5 + num_1

    return total_num


if __name__ == '__main__':
    # m = int(sys.stdin.read())
    m = int(input())
    print(get_change(m))
