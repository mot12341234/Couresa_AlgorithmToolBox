# Uses python3
import sys

# def fibonacci_partial_sum_naive(from_, to):
#     sum = 0
#
#     current = 0
#     next  = 1
#
#     for i in range(to + 1):
#         if i >= from_:
#             sum += current
#
#         current, next = next, current + next
#
#     return sum % 10


def fibonacci_partial_sum(m, n):

    # e.g. m = 3, n = 7 -> F(9) - F(4)
    last_digit = [0] * (61)
    last_digit[1] = 1

    for i in range(2, 61):
        last_digit[i] = (last_digit[i-1] + last_digit[i-2]) % 10

    if m == 0:
        last_digit_1 = 0
    elif m == 1:
        last_digit_1 = 0
    else:
        new_m = (m + 1) % 60
        if last_digit[new_m] == 0:
            last_digit_1 = 9
        else:
            last_digit_1 = last_digit[new_m] - 1

    new_n = (n + 2)% 60
    if last_digit[new_n] == 0:
        last_digit_2 = 9
    else:
        last_digit_2 = last_digit[new_n] - 1

    if last_digit_2 < last_digit_1:
        return last_digit_2 + 10 - last_digit_1

    else:
        return last_digit_2 - last_digit_1


if __name__ == '__main__':
    # input = sys.stdin.read()
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum(from_, to))