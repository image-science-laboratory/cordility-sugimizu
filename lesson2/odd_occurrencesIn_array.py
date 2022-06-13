# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    A_count = {}

    for i in A:
        if str(i) in A_count:
            A_count[str(i)] += 1
        else:
            A_count[str(i)] = 1

    result = -1
    for key, value in A_count.items():
        if (value % 2) == 1:
            result = int(key)
            break

    return result
