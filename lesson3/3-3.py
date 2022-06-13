# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    result = 999999999999999999
    sum_whole = sum([n for n in A])

    for p in range(1, len(A)):
        sum_left = sum([A[n] for n in range(0, p)])
        if abs(2 * sum_left - sum_whole) < result:
            result = abs(2 * sum_left - sum_whole)

    return result


# print(solution([3, 1, 2, 4, 3]))
