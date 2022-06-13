# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    A.sort()

    result = 1
    if len(A) != 0:
        for i in range(len(A)):
            if A[i] != (i + 1):
                result = i + 1
                break

            # last element が missing の場合
            result = len(A) + 1

    return result
