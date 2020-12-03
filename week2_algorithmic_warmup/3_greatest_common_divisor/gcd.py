# Uses python3
import sys


# def gcd_naive(a, b):
#     current_gcd = 1
#     for d in range(2, min(a, b) + 1):
#         if a % d == 0 and b % d == 0:
#             if d > current_gcd:
#                 current_gcd = d
#
#     return current_gcd

def gcd(a, b):
    # Euclidean Algorithm
    # 100, 30 -> 30, 10 -> 10
    result = max(a, b) % min(a, b)
    if result == 0:
        return min(a, b)
    else:
        return gcd(result, min(a, b))


if __name__ == "__main__":
    # input = sys.stdin.read()
    a, b = map(int, input().split())
    print(gcd(a, b))
