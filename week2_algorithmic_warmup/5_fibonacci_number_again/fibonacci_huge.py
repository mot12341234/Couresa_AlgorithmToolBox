# Uses python3
import sys

# def get_fibonacci_huge_naive(n, m):
#     if n <= 1:
#         return n
#
#     previous = 0
#     current  = 1
#
#     for _ in range(n - 1):
#         previous, current = current, previous + current
#
#     return current % m

def find_pisano_period(m):
    # a pisano period starts with 01

    previous, current = 0, 1
    for i in range(m * m):
        previous, current = current, (previous + current) % m

        if previous == 0 and current == 1:
            return i + 1


def get_fibonacci_huge(n, m):

    pisano_period = find_pisano_period(m)

    new_n = n % pisano_period

    if new_n == 0:
        return 0
    elif new_n == 1:
        return 1
    else:
        result = [0] * (new_n + 1)

        result[0] = 0
        result[1] = 1

        for i in range(2, new_n + 1):
            result[i] = (result[i-1] + result[i-2]) % m

        return result[new_n]


if __name__ == '__main__':
    # input = sys.stdin.read();
    n, m = map(int, input().split())
    print(get_fibonacci_huge(n, m))
