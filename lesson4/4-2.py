# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # # O(n**2)
    # for i in range(1, len(A) + 1):
    #     if i not in A:
    #         return 0

    dic = {}

    for i in A:
        dic[i] = True

    for i in range(1, len(A) + 1):
        if i not in dic:
            return 0

    return 1
