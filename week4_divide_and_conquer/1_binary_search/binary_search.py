# Uses python3
import sys


def binary_search(keys, query):
    left, right = 0, len(keys) - 1

    result = -1
    while left <= right:
        middle = (right + left) // 2

        if query == keys[middle]:
            result = middle
            return result
        elif query > keys[middle]:
            left = middle + 1
        elif query < keys[middle]:
            right = middle - 1

    return result


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]
    for query in input_queries:
        # replace with the call to binary_search when implemented
        print(binary_search(input_keys, query), end=' ')
