# Uses python3
import sys


# def lcm_naive(a, b):
#     for l in range(1, a*b + 1):
#         if l % a == 0 and l % b == 0:
#             return l
#
#     return a*b

def gcd(a, b):
    result = max(a, b) % min(a, b)
    if result == 0:
        return min(a, b)
    else:
        return gcd(min(a, b), result)


def lcm(a, b):

    greatCommonDivisor = gcd(a, b)

    return a * b // greatCommonDivisor


if __name__ == '__main__':
    # input = sys.stdin.read()
    a, b = map(int, input().split())
    print(lcm(a, b))

