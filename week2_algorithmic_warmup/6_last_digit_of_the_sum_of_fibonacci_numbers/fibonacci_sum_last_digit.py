# Uses python3
import sys

# def fibonacci_sum_naive(n):
#     if n <= 1:
#         return n
#
#     previous = 0
#     current  = 1
#     sum      = 1
#
#     for _ in range(n - 1):
#         previous, current = current, previous + current
#         sum += current
#
#     return sum % 10

def find_pisano_period(m):

    previous = 0
    current = 1

    for i in range(m * m):
        previous, current = current, (previous + current) % m

        if previous == 0 and current == 1:
            return i + 1


def fibonacci_sum(n):
    # sum of nth Fib num = F(n+2) - 1
    # a1 + a2 = a3
    # a4 = a2 + a3 = a0 + a1 + a1 + a2 = a0 + a1 + a2 + (a1) = F(2) + 1

    pisano_period = find_pisano_period(10)

    new_n = (n+2) % pisano_period

    result = [0] * (new_n + 1)
    result[1] = 1

    for i in range(2, new_n + 1):
        result[i] = (result[i-1] + result[i-2]) % 10

    result[new_n] -= 1
    if result[new_n] < 0:
        return 9

    return result[new_n]


if __name__ == '__main__':
    # input = sys.stdin.read()
    n = int(input())
    print(fibonacci_sum(n))
