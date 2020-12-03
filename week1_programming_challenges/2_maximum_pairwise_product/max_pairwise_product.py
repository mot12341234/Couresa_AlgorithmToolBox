# python3


# def max_pairwise_product(numbers):
#     n = len(numbers)
#     max_product = 0
#     for first in range(n):
#         for second in range(first + 1, n):
#             max_product = max(max_product,
#                 numbers[first] * numbers[second])
#
#     return max_product


def max_pairwise_product(numbers):
    maxIndex = 0
    n = len(numbers)

    for i in range(n):
        if numbers[i] > numbers[maxIndex]:
            maxIndex = i

    if maxIndex == 0:
        secMaxIndex = 1
    else:
        secMaxIndex = 0

    for i in range(n):
        if numbers[i] > numbers[secMaxIndex] and i != maxIndex:
            secMaxIndex = i

    return numbers[maxIndex] * numbers[secMaxIndex]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
