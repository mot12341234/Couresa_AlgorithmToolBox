# Uses python3
from sys import stdin

# def fibonacci_sum_squares_naive(n):
#     if n <= 1:
#         return n
#
#     previous = 0
#     current  = 1
#     sum      = 1
#
#     for _ in range(n - 1):
#         previous, current = current, previous + current
#         sum += current * current
#
#     return sum % 10


def fibonacci_sum_squares(n):

    # result = the last digit of n * (n+1)

    last_digit = [0] * 61
    last_digit[1] = 1

    for i in range(2, 61):
        last_digit[i] = (last_digit[i-1] + last_digit[i-2]) % 10

    num_1 = last_digit[n % 60]
    num_2 = last_digit[(n+1) % 60]

    return (num_1 * num_2) % 10


if __name__ == '__main__':
    # n = int(stdin.read())
    n = int(input())
    print(fibonacci_sum_squares(n))
