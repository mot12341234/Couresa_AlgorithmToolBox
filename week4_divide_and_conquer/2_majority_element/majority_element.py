# Uses python3
import sys


def get_majority_element(a, left, right):
    if left == right:
        return -1
    elif left + 1 == right:
        return a[left]

    # split A into two pars A1, A2
    # if v is the majority element of A, it must also be a majority element of A1 or A2 or both

    middle = (left + right) // 2

    left = get_majority_element(a, left, middle)
    right = get_majority_element(a, middle, right)

    # count the occurrence of left and right element
    c1, c2 = 0, 0

    for i in a[left:right]:
        if i == left:
            c1 += 1
        elif i == right:
            c2 += 1

    if c1 > (right - left) // 2 and left != -1:
        return left
    elif c2 > (right - left) // 2 and right != -1:
        return right
    else:
        return -1


if __name__ == '__main__':
    # input = sys.stdin.read()
    n, *a = list(map(int, input().split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)


# e.g. 2, 3, 9, 2, 2
# left = 0, right = 5, middle = 2
# f(a, 0, 5)
# f(a, 0, 1) = 2 & f(a, 1, 2) = 3 ---> f(a, 0, 2) = -1
# f(a, 2, 3) = 9 & f(a, 3, 5) = 2 ---> f(a, 2, 5) = 2
# f(a, 0, 2) = -1 & f(a, 2, 5) = 2 ---> f(a, 0, 5) = 2

#  -> , f(a, 2, 5)
